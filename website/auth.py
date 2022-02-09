from flask import Blueprint, request, flash, render_template

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)


@auth.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        name = request.form.get('Name')
        surname = request.form.get('Surname')
        address = request.form.get('Address')
        date = request.form.get('Date')
        gender = request.form.get('Gender')
        telephone = request.form.get('Telephone')
        taxcode = request.form.get('Taxcode')
        email = request.form.get('Email')
        password = request.form.get('Password')
        flash('Account creato!', category="success")

    return render_template('signin.html')


@auth.route("/signinlocal", methods=['GET', 'POST'])
def signinlocal():
    if request.method == 'POST':
        name = request.form.get('Name')
        surname = request.form.get('Surname')
        address = request.form.get('Address')
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
        address = request.form.get('Address')
        date = request.form.get('Date')
        gender = request.form.get('Gender')
        telephone = request.form.get('Telephone')
        taxcode = request.form.get('Taxcode')
        document = request.form.get('Document')
        iban = request.form.get('Iban')
        email = request.form.get('Email')
        password = request.form.get('Password')

    return render_template('signinrider.html')
