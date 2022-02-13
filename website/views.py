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
@login_required
def customereditprofile():
    return render_template('customereditprofile.html')

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
