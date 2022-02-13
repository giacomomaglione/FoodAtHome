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

@views.route("/customerindex")
@login_required
def customerindex():
    return render_template('customerindex.html')

@views.route("/customereditprofile")
@login_required
def customereditprofile():
    return render_template('customereditprofile.html')

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
            utente = cliente.find_one(current_user['Email'])
            if name is None :
                utente = cliente.update({'Name': utente['Name']}, {"$set": name})













    return render_template('editprofile.html' , form=form)







    return render_template('editprofile.html')

@views.route("/riderindex")
@login_required
def riderindex():
    return render_template('riderindex.html')

@views.route("/ridereditprofile")
@login_required
def ridereditprofile():
    return render_template('ridereditprofile.html')

@views.route("/localindex")
@login_required
def localindex():
    return render_template('localindex.html')

@views.route("/localeditprofile")
@login_required
def localeditprofile():
    return render_template('localeditprofile.html')
