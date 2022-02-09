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

        if len(email)<4:
            flash("L'email deve essere di almeno 4 caratteri!", category="error")
        elif len(name)<3:
            flash("Il nome deve essere di almeno 3 caratteri!", category="error")
        elif len(password)<7:
            flash("La password deve essere di almeno 7 caratteri!", category="error")
        elif
            flash('Account creato!', category="success")

        account = {"Name": name, "Surname": , "Street": "Via Milano, 32", "City": "Napoli", "Province": "Napoli", "Birthday": "07/02/2000", "Gender": "M", "PhoneNumber": 3334567890, "TaxCode": "RSSMRA00B07F839U", "Email": "mario.rossi@alice.it", "Password": "Mario00R"}
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

        if len(email)<4:
            flash("L'email deve essere di almeno 4 caratteri!", category="error")
        elif len(name)<3:
            flash("Il nome deve essere di almeno 3 caratteri!", category="error")
        elif len(password)<7:
            flash("La password deve essere di almeno 7 caratteri!", category="error")
        elif
            flash('Account creato!', category="success")

        account = {"Name": name}
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

        if len(email)<4:
            flash("L'email deve essere di almeno 4 caratteri!", category="error")
        elif len(name)<3:
            flash("Il nome deve essere di almeno 3 caratteri!", category="error")
        elif len(password)<7:
            flash("La password deve essere di almeno 7 caratteri!", category="error")
        elif
            flash('Account creato!', category="success")

        account = {"Name": name}
        rider.insert_one(account)

    return render_template('signinrider.html')
