from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, login_user
from .form import EditProfile
from . import cliente, rider, negozio
from .models import Cliente, Rider, Local
from . import login


views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template('index.html')

@views.route("/aboutus")
def about():
    return render_template('aboutus.html')


@views.route("/editprofile", methods=['GET', 'POST'])
@login_required
def editprofile():
    form = EditProfile()
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
        localname = form.localname.data
        piva = form.piva.data




        print(password)

        if current_user.type == 0 :
            utente = cliente.find_one({"Email" : current_user.Email})
            if name is not "" :
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street is not "":
               cliente.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender is not None:
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password is not "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
        if current_user.type == 1 :
            utente = rider.find_one({"Email" : current_user.Email})
            if name is not "" :
                rider.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street is not "":
               rider.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender is not None:
                rider.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban is not "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})
        if current_user.type == 2:
            utente = negozio.find_one({"Email": current_user.Email})
            if name is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender is not None:
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})
            if piva is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IVA": piva}})
            if localname is not "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"LocalName": localname}})


    return render_template('editprofile.html' , form=form)


@views.route("/riderindex")
@login_required
def riderindex():
    return render_template('riderindex.html')


@views.route("/localindex")
@login_required
def localindex():
    return render_template('localindex.html')

@views.route("/customerindex")
@login_required
def customerindex():
    return render_template('customerindex.html')