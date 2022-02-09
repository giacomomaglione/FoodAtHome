from flask import Blueprint, request, flash, render_template
from pymongo import MongoClient

auth = Blueprint('auth', __name__)

connessione = MongoClient("mongodb://localhost:27017/")
database = connessione["foodathome"]
cliente = database["Customer"]

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
        flash('Account creato!', category="success")
        account = {"Name": name}
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

    return render_template('signinrider.html')
