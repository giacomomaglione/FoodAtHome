from flask import Blueprint, request, flash, render_template, redirect, url_for
# from pymongo import MongoClient
#from __init__ import app
import certifi
from website import database
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#connessione = MongoClient("mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test",
 #                         tlsCAFile=certifi.where())

#database = connessione["foodathome"]
cliente = database.Database.DATABASE["Customer"]
rider = database.Database.DATABASE["Rider"]
negozio = database.Database.DATABASE["Store"]


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = cliente.find_one({"Email": email})

        if user is None:
            flash('Email non registrata', category="error")
        else:
            if user["Email"] == email:
                if user["Password"] == password:
                    flash('Accesso eseguito', category="success")
                    #login_user(user, remember=True)
                    #return redirect(url_for('views.clentindex'))
                else:
                    flash('Password incorretta', category="error")

    return render_template('login.html', boolean=True)


@auth.route("/loginrider", methods=['GET', 'POST'])
def loginrider():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = rider.find_one({"Email": email})

        if user is None:
            flash('Email non registrata', category="error")
        else:
            if user["Email"] == email:
                if user["Password"] == password:
                    flash('Accesso eseguito', category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.riderindex'))
                else:
                    flash('Password incorretta', category="error")

    return render_template('login.html', boolean=True)


@auth.route("/loginshop", methods=['GET', 'POST'])
def loginshop():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = negozio.find_one({"Email": email})

        if user is None:
            flash('Email non registrata', category="error")
        else:
            if user["Email"] == email:
                if user["Password"] == password:
                    flash('Accesso eseguito', category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.localindex'))
                else:
                    flash('Password incorretta', category="error")

    return render_template('login.html', boolean=True)


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


@auth.route("/signinlocal", methods=['GET', 'POST'])
def signinlocal():
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
        document = request.form.get('Document')
        iban = request.form.get('Iban')
        iva = request.form.get('Iva')
        localname = request.form.get('LocalName')
        email = request.form.get('Email')
        password = request.form.get('Password')

        if len(email) < 4:
            flash("L'email deve essere di almeno 4 caratteri!", category="error")
        elif len(name) < 3:
            flash("Il nome deve essere di almeno 3 caratteri!", category="error")
        elif len(password) < 7:
            flash("La password deve essere di almeno 7 caratteri!", category="error")
        else:
            flash('Account creato!', category="success")

        account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                   "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode, "ID": document,
                   "IBAN": iban, "IVA": iva, "LocalName": localname, "Email": email, "Password": password}
        negozio.insert_one(account)

    return render_template('signinlocal.html')


@auth.route("/signinrider", methods=['GET', 'POST'])
def signinrider():
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
        document = request.form.get('Document')
        iban = request.form.get('Iban')
        email = request.form.get('Email')
        password = request.form.get('Password')

        if len(email) < 4:
            flash("L'email deve essere di almeno 4 caratteri!", category="error")
        elif len(name) < 3:
            flash("Il nome deve essere di almeno 3 caratteri!", category="error")
        elif len(password) < 7:
            flash("La password deve essere di almeno 7 caratteri!", category="error")
        else:
            flash('Account creato!', category="success")

        account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                   "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode, "ID": document,
                   "IBAN": iban, "Email": email, "Password": password}
        rider.insert_one(account)

    return render_template('signinrider.html')
