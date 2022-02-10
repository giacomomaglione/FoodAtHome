from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template('index.html')


@views.route("/aboutus")
def about():
    return render_template('aboutus.html')

@views.route("/clientindex")
@login_required
def clientindex():
    return render_template('clientindex.html')

@views.route("/riderindex")
@login_required
def riderindex():
    return render_template('riderindex.html')

@views.route("/localindex")
@login_required
def localindex():
    return render_template('localindex.html')
