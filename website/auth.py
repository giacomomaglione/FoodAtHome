from flask import Blueprint, redirect
from flask import render_template, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from .form import Login
from werkzeug.urls import url_parse
from . import cliente
from .models import Cliente # NON LO CANCELLARE; Missing user_loader or request_loader

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    print(form.email)
    print(form.password)
    if form.validate_on_submit():
        user = cliente.find_one({"Email": request.form.get('Email')})
        if user and user["Password"] == request.form.get('Email'):
            user_obj = Cliente(username=user['Email'])
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash("Invalid username or password")
    else:
        flash("validate_on_submit")
    return render_template('login.html', form = form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))

@auth.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        name = request.form.get('Name')
        surname = request.form.get('Surname')
        street = request.form.get('Street')
        city = request.form.get('City')
        province = request.form.get('Province')
        date = request.form.get('Date')
        gender = request.form.get('Gender')
        telephone = request.form.get('Telephone')
        taxcode = request.form.get('Taxcode')
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = cliente.find_one({"Email": email})

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
        else:
            flash("Email già registrata", category="error")

    return render_template('signin.html')
