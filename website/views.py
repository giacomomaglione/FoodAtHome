from flask import Blueprint, render_template
from flask_login import login_required

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
def customereditprofile():
    return render_template('customereditprofile.html')

@views.route("/riderindex")
def riderindex():
    return render_template('riderindex.html')

@views.route("/ridereditprofile")
def ridereditprofile():
    return render_template('ridereditprofile.html')

@views.route("/localindex")
def localindex():
    return render_template('localindex.html')

@views.route("/localeditprofile")
def localeditprofile():
    return render_template('localeditprofile.html')
