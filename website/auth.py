from flask import Blueprint, redirect
from flask import render_template, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from .form import Login, ClientSigninForm, RiderSigninForm
from werkzeug.urls import url_parse
from . import cliente, rider, negozio
from .models import Cliente, Rider # NON LO CANCELLARE; Missing user_loader or request_loader

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()

    formemail = form.email.data
    formpassword = form.password.data

    if form.validate_on_submit():
        user = cliente.find_one({"Email": formemail})

        if not user:
            flash("Email non registrata", category='error')

        elif user["Password"] == formpassword:
            flash("Accesso Eseguito")
            user_obj = Cliente(username=user['Email'])
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('views.customerindex')
            return redirect(next_page)
        else:
            flash("Password Errata", category='error')

    return render_template('login.html', form = form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))

@auth.route("/signin", methods=['GET', 'POST'])
def signin():

    form = ClientSigninForm()

    if request.method == 'POST':

        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = form.password.data

        user = cliente.find_one({"Email": form.email.data})

        if user is None:
            if len(email) < 3:
                flash("L'email deve essere di almeno 4 caratteri!", category="error")
            elif len(name) < 3:
                flash("Il nome deve essere di almeno 3 caratteri!", category="error")
            elif len(password) < 7:
                flash("La password deve essere di almeno 7 caratteri!", category="error")
            else:
                flash('Account creato!', category="success")

                account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                           "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode,
                           "Email": email, "Password": password}
                cliente.insert_one(account)
                return redirect('views.index')
        else:
            flash("Email già registrata", category="error")

    return render_template('signin.html' , form=form)


@auth.route("/loginrider", methods=['GET', 'POST'])
def loginrider():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()

    formemail = form.email.data
    formpassword = form.password.data

    if form.validate_on_submit():
        user = rider.find_one({"Email": formemail})

        if not user:
            flash("Email non registrata", category='error')

        elif user["Password"] == formpassword:
            flash("Accesso Eseguito")
            user_obj = Rider(username=user['Email'])
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('views.riderindex')
            return redirect(next_page)
        else:
            flash("Password Errata", category='error')

    return render_template('loginrider.html', form = form)

@auth.route("/signinrider", methods=['GET', 'POST'])
def signinrider():

    form = RiderSigninForm()

    if request.method == 'POST':

        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = form.password.data
        id = form.id.data
        iban = form.iban.data

        user = rider.find_one({"Email": form.email.data})

        if user is None:
            if len(email) < 3:
                flash("L'email deve essere di almeno 4 caratteri!", category="error")
            elif len(name) < 3:
                flash("Il nome deve essere di almeno 3 caratteri!", category="error")
            elif len(password) < 7:
                flash("La password deve essere di almeno 7 caratteri!", category="error")
            else:
                flash('Account creato!', category="success")

                account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                           "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode,
                           "Email": email, "Password": password, "ID": id, "IBAN" : iban}
                rider.insert_one(account)
                return redirect('views.index')
        else:
            flash("Email già registrata", category="error")

    return render_template('signinrider.html' , form=form)