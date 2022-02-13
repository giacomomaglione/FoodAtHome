from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user
from .form import EditProfile
from . import cliente, rider, negozio, prodotto
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

        if current_user.type == 0 :
            utente = cliente.find_one({"Email" : current_user.Email})
            if name != "" :
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
                form.name.data=""
            if surname != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street != "":
               cliente.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender !=  None:
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})

        if current_user.type == 1 :
            utente = rider.find_one({"Email" : current_user.Email})
            if name !=  "" :
                rider.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street !=  "":
               rider.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender != None:
                rider.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id != "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban != "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})

        if current_user.type == 2:
            utente = negozio.find_one({"Email": current_user.Email})
            if name != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender != None:
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})
            if piva != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IVA": piva}})
            if localname != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"LocalName": localname}})
    return render_template('editprofile.html' , form=form)


@views.route("/riderindex")
@login_required
def riderindex():
    if current_user.type != 1:
        return redirect(url_for('views.index'))
    return render_template('riderindex.html')


@views.route("/localindex", methods=['GET', 'POST'])
@login_required
def localindex():
    if current_user.type != 2:
        return redirect(url_for('views.index'))

    prod_query = prodotto.find({"Store": current_user.Email})
    list = []
    for prod in prod_query:
        list.append(prod)
        #print(prod['Name'])

    return render_template('localindex.html', list=list)

@views.route("/customerindex")
@login_required
def customerindex():
    if current_user.type != 0:
        return redirect(url_for('views.index'))
    return render_template('customerindex.html')