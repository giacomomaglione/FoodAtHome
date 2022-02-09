from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/aboutus")
def about():
    return render_template('aboutus.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)


@app.route("/signin", methods=['GET', 'POST'])
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


@app.route("/signinlocal", methods=['GET', 'POST'])
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


@app.route("/signinrider", methods=['GET', 'POST'])
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


if __name__ == "__main__":
    app.run()
