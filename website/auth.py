from flask import Blueprint, request, flash, render_template
from pymongo import MongoClient

auth = Blueprint('auth', __name__)

connessione = MongoClient("mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test")
database = connessione["foodathome"]
cliente = database["Customer"]
rider = database["Rider"]
negozio = database["Store"]


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = collection.find_one({"Email":email, "Password":password})
        if user:
            if check_password_hash(user.password, password)
                flash('Accesso eseguito', category=success)
                else:
                    flash('Password incorretta', category=error)
        else:
        flash('Email non registrata', category=error)

    return render_template('login.html', boolean=True)


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

        user = collection.find_one({"Email": email, "Password": password})
        if user:
            flash("Email già registrata", category="error")
    else:
        flash('Email non registrata', category=error)

        elif len(email) < 4:
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
