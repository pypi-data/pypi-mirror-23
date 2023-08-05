"""
The blueprint for the web interface.

Contains all the interaction logic with the end user (except forms which
are directly handled in the forms module.

Basically, this blueprint takes care of the authentication and provides
some shortcuts to make your life better when coding (see `pull_project`
and `add_project_id` for a quick overview)
"""

from flask import Blueprint, current_app, flash, g, redirect, \
    render_template, request, session, url_for, send_file
from flask_mail import Mail, Message
from flask_babel import get_locale, gettext as _
from smtplib import SMTPRecipientsRefused
import werkzeug
from sqlalchemy import orm
from functools import wraps

# local modules
from models import db, Project, Person, Bill
from forms import AdminAuthenticationForm, AuthenticationForm, EditProjectForm, \
    InviteForm, MemberForm, PasswordReminder, ProjectForm, get_billform_for, \
    ExportForm
from utils import Redirect303, list_of_dicts2json, list_of_dicts2csv

main = Blueprint("main", __name__)
mail = Mail()


def requires_admin(f):
    """Require admin permissions for @requires_admin decorated endpoints.
       Has no effect if ADMIN_PASSWORD is empty (default value)
    """
    @wraps(f)
    def admin_auth(*args, **kws):
        admin_password = session.get('admin_password', '')
        if not admin_password == current_app.config['ADMIN_PASSWORD']:
            raise Redirect303(url_for('.admin', goto=request.path))
        return f(*args, **kws)
    return admin_auth


@main.url_defaults
def add_project_id(endpoint, values):
    """Add the project id to the url calls if it is expected.

    This is to not carry it everywhere in the templates.
    """
    if 'project_id' in values or not hasattr(g, 'project'):
        return
    if current_app.url_map.is_endpoint_expecting(endpoint, 'project_id'):
        values['project_id'] = g.project.id


@main.url_value_preprocessor
def pull_project(endpoint, values):
    """When a request contains a project_id value, transform it directly
    into a project by checking the credentials are stored in session.

    If not, redirect the user to an authentication form
    """
    if endpoint == "authenticate":
        return
    if not values:
        values = {}
    project_id = values.pop('project_id', None)
    if project_id:
        project = Project.query.get(project_id)
        if not project:
            raise Redirect303(url_for(".create_project",
                project_id=project_id))
        if project.id in session and session[project.id] == project.password:
            # add project into kwargs and call the original function
            g.project = project
        else:
            # redirect to authentication page
            raise Redirect303(
                    url_for(".authenticate", project_id=project_id))


@main.route("/admin", methods=["GET", "POST"])
def admin():
    """Admin authentication"""
    form = AdminAuthenticationForm()
    goto = request.args.get('goto', url_for('.home'))
    if request.method == "POST":
        if form.validate():
            if form.admin_password.data == current_app.config['ADMIN_PASSWORD']:
                session['admin_password'] = form.admin_password.data
                session.update()
                return redirect(goto)
            else:
                msg = _("This admin password is not the right one")
                form.errors['admin_password'] = [msg]
    return render_template("authenticate.html", form=form, admin_auth=True)


@main.route("/authenticate", methods=["GET", "POST"])
def authenticate(project_id=None):
    """Authentication form"""
    form = AuthenticationForm()
    if not form.id.data and request.args.get('project_id'):
        form.id.data = request.args['project_id']
    project_id = form.id.data
    if project_id is None:
        #User doesn't provide project identifier, return to authenticate form
        msg = _("You need to enter a project identifier")
        form.errors["id"] = [msg]
        return render_template("authenticate.html", form=form)
    else:
        project = Project.query.get(project_id)

    create_project = False  # We don't want to create the project by default
    if not project:
        # But if the user try to connect to an unexisting project, we will
        # propose him a link to the creation form.
        if request.method == "POST":
            form.validate()
        else:
            create_project = project_id

    else:
        # if credentials are already in session, redirect
        if project_id in session and project.password == session[project_id]:
            setattr(g, 'project', project)
            return redirect(url_for(".list_bills"))

        # else process the form
        if request.method == "POST":
            if form.validate():
                if not form.password.data == project.password:
                    msg = _("This private code is not the right one")
                    form.errors['password'] = [msg]
                else:
                    # maintain a list of visited projects
                    if "projects" not in session:
                        session["projects"] = []
                    # add the project on the top of the list
                    session["projects"].insert(0, (project_id, project.name))
                    session[project_id] = form.password.data
                    session.update()
                    setattr(g, 'project', project)
                    return redirect(url_for(".list_bills"))

    return render_template("authenticate.html", form=form,
            create_project=create_project)


@main.route("/")
def home():
    project_form = ProjectForm()
    auth_form = AuthenticationForm()
    # If ADMIN_PASSWORD is empty we consider that admin mode is disabled
    is_admin_mode_enabled = bool(current_app.config['ADMIN_PASSWORD'])
    is_demo_project_activated = current_app.config['ACTIVATE_DEMO_PROJECT']

    return render_template("home.html", project_form=project_form,
                           is_demo_project_activated=is_demo_project_activated,
                           is_admin_mode_enabled=is_admin_mode_enabled,
                           auth_form=auth_form, session=session)


@main.route("/create", methods=["GET", "POST"])
@requires_admin
def create_project():
    form = ProjectForm()
    if request.method == "GET" and 'project_id' in request.values:
        form.name.data = request.values['project_id']

    if request.method == "POST":
        # At first, we don't want the user to bother with the identifier
        # so it will automatically be missing because not displayed into
        # the form
        # Thus we fill it with the same value as the filled name,
        # the validation will take care of the slug
        if not form.id.data:
            form.id.data = form.name.data
        if form.validate():
            # save the object in the db
            project = form.save()
            db.session.add(project)
            db.session.commit()

            # create the session object (authenticate)
            session[project.id] = project.password
            session.update()

            # send reminder email
            g.project = project

            message_title = _("You have just created '%(project)s' "
                "to share your expenses", project=g.project.name)

            message_body = render_template("reminder_mail.%s" %
                get_locale().language)

            msg = Message(message_title,
                body=message_body,
                recipients=[project.contact_email])
            try:
                mail.send(msg)
            except SMTPRecipientsRefused:
                msg_compl = 'Problem sending mail. '
                # TODO: destroy the project and cancel instead?
            else:
                msg_compl = ''

            # redirect the user to the next step (invite)
            flash(_("%(msg_compl)sThe project identifier is %(project)s",
                msg_compl=msg_compl, project=project.id))
            return redirect(url_for(".invite", project_id=project.id))

    return render_template("create_project.html", form=form)


@main.route("/password-reminder", methods=["GET", "POST"])
def remind_password():
    form = PasswordReminder()
    if request.method == "POST":
        if form.validate():
            # get the project
            project = Project.query.get(form.id.data)

            # send the password reminder
            password_reminder = "password_reminder.%s" % get_locale().language
            mail.send(Message("password recovery",
                body=render_template(password_reminder, project=project),
                recipients=[project.contact_email]))
            flash(_("a mail has been sent to you with the password"))

    return render_template("password_reminder.html", form=form)


@main.route("/<project_id>/edit", methods=["GET", "POST"])
def edit_project():
    edit_form = EditProjectForm()
    export_form = ExportForm()
    if request.method == "POST":
        if edit_form.validate():
            project = edit_form.update(g.project)
            db.session.commit()
            session[project.id] = project.password

            return redirect(url_for(".list_bills"))

        if export_form.validate():
            export_format = export_form.export_format.data
            export_type = export_form.export_type.data

            if export_type == 'transactions':
                export = g.project.get_transactions_to_settle_bill(
                    pretty_output=True)
            if export_type == "bills":
                export = g.project.get_pretty_bills(
                    export_format=export_format)

            if export_format == "json":
                file2export = list_of_dicts2json(export)
            if export_format == "csv":
                file2export = list_of_dicts2csv(export)

            return send_file(file2export,
                             attachment_filename="%s-%s.%s" %
                             (g.project.id, export_type, export_format),
                             as_attachment=True
                            )
    else:
        edit_form.name.data = g.project.name
        edit_form.password.data = g.project.password
        edit_form.contact_email.data = g.project.contact_email

    return render_template("edit_project.html", edit_form=edit_form, export_form=export_form)


@main.route("/<project_id>/delete")
def delete_project():
    g.project.remove_project()
    flash(_('Project successfully deleted'))

    return redirect(url_for(".home"))


@main.route("/exit")
def exit():
    # delete the session
    session.clear()
    return redirect(url_for(".home"))


@main.route("/demo")
def demo():
    """
    Authenticate the user for the demonstration project and redirect him to
    the bills list for this project.

    Create a demo project if it doesnt exists yet (or has been deleted)
    If the demo project is deactivated, one is redirected to the create project form
    """
    is_demo_project_activated = current_app.config['ACTIVATE_DEMO_PROJECT']
    project = Project.query.get("demo")

    if not project and not is_demo_project_activated:
        raise Redirect303(url_for(".create_project",
                                  project_id='demo'))
    if not project and is_demo_project_activated:
        project = Project(id="demo", name=u"demonstration", password="demo",
                contact_email="demo@notmyidea.org")
        db.session.add(project)
        db.session.commit()
    session[project.id] = project.password
    return redirect(url_for(".list_bills", project_id=project.id))


@main.route("/<project_id>/invite", methods=["GET", "POST"])
def invite():
    """Send invitations for this particular project"""

    form = InviteForm()

    if request.method == "POST":
        if form.validate():
            # send the email

            message_body = render_template("invitation_mail.%s" %
                get_locale().language)

            message_title = _("You have been invited to share your "
                "expenses for %(project)s", project=g.project.name)
            msg = Message(message_title,
                body=message_body,
                recipients=[email.strip()
                    for email in form.emails.data.split(",")])
            mail.send(msg)
            flash(_("Your invitations have been sent"))
            return redirect(url_for(".list_bills"))

    return render_template("send_invites.html", form=form)


@main.route("/<project_id>/")
def list_bills():
    bill_form = get_billform_for(g.project)
    # set the last selected payer as default choice if exists
    if 'last_selected_payer' in session:
        bill_form.payer.data = session['last_selected_payer']
    # Preload the "owers" relationship for all bills
    bills = g.project.get_bills().options(orm.subqueryload(Bill.owers))

    return render_template("list_bills.html",
            bills=bills, member_form=MemberForm(g.project),
            bill_form=bill_form,
            add_bill=request.values.get('add_bill', False),
            current_view="list_bills",
    )


@main.route("/<project_id>/members/add", methods=["GET", "POST"])
def add_member():
    # FIXME manage form errors on the list_bills page
    form = MemberForm(g.project)
    if request.method == "POST":
        if form.validate():
            member = form.save(g.project, Person())
            db.session.commit()
            flash(_("%(member)s had been added", member=member.name))
            return redirect(url_for(".list_bills"))

    return render_template("add_member.html", form=form)


@main.route("/<project_id>/members/<member_id>/reactivate", methods=["POST"])
def reactivate(member_id):
    person = Person.query.filter(Person.id == member_id)\
                .filter(Project.id == g.project.id).all()
    if person:
        person[0].activated = True
        db.session.commit()
        flash(_("%(name)s is part of this project again", name=person[0].name))
    return redirect(url_for(".list_bills"))


@main.route("/<project_id>/members/<member_id>/delete", methods=["POST"])
def remove_member(member_id):
    member = g.project.remove_member(member_id)
    if member:
        if member.activated == False:
            flash(_("User '%(name)s' has been deactivated", name=member.name))
        else:
            flash(_("User '%(name)s' has been removed", name=member.name))
    return redirect(url_for(".list_bills"))


@main.route("/<project_id>/members/<member_id>/edit",
            methods=["POST", "GET"])
def edit_member(member_id):
    member = Person.query.get(member_id, g.project)
    if not member:
        raise werkzeug.exceptions.NotFound()
    form = MemberForm(g.project, edit=True)

    if request.method == 'POST' and form.validate():
        form.save(g.project, member)
        db.session.commit()
        flash(_("User '%(name)s' has been edited", name=member.name))
        return redirect(url_for(".list_bills"))

    form.fill(member)
    return render_template("edit_member.html", form=form, edit=True)


@main.route("/<project_id>/add", methods=["GET", "POST"])
def add_bill():
    form = get_billform_for(g.project)
    if request.method == 'POST':
        if form.validate():
            # save last selected payer in session
            session['last_selected_payer'] = form.payer.data
            session.update()

            bill = Bill()
            db.session.add(form.save(bill, g.project))
            db.session.commit()

            flash(_("The bill has been added"))

            args = {}
            if form.submit2.data:
                args['add_bill'] = True

            return redirect(url_for('.list_bills', **args))

    return render_template("add_bill.html", form=form)


@main.route("/<project_id>/delete/<int:bill_id>")
def delete_bill(bill_id):
    # fixme: everyone is able to delete a bill
    bill = Bill.query.get(g.project, bill_id)
    if not bill:
        raise werkzeug.exceptions.NotFound()

    db.session.delete(bill)
    db.session.commit()
    flash(_("The bill has been deleted"))

    return redirect(url_for('.list_bills'))


@main.route("/<project_id>/edit/<int:bill_id>", methods=["GET", "POST"])
def edit_bill(bill_id):
    # FIXME: Test this bill belongs to this project !
    bill = Bill.query.get(g.project, bill_id)
    if not bill:
        raise werkzeug.exceptions.NotFound()

    form = get_billform_for(g.project, set_default=False)

    if request.method == 'POST' and form.validate():
        form.save(bill, g.project)
        db.session.commit()

        flash(_("The bill has been modified"))
        return redirect(url_for('.list_bills'))

    if not form.errors:
        form.fill(bill)

    return render_template("add_bill.html", form=form, edit=True)


@main.route("/lang/<lang>")
def change_lang(lang):
    session['lang'] = lang
    session.update()

    return redirect(request.headers.get('Referer') or url_for('.home'))


@main.route("/<project_id>/settle_bills")
def settle_bill():
    """Compute the sum each one have to pay to each other and display it"""
    bills = g.project.get_transactions_to_settle_bill()
    return render_template(
        "settle_bills.html",
        bills=bills,
        current_view='settle_bill',
    )


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", projects=Project.query.all())
