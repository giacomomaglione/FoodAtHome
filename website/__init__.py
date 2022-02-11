from website import database
from flask import Flask, render_template, session, redirect
from flask_session import Session

from functools import wraps

database.Database.initialize()

cliente= database.Database.DATABASE["Customer"]
rider = database.Database.DATABASE["Rider"]
negozio = database.Database.DATABASE["Store"]

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BNRD gnmldesw HUgI HSNsgs'
    app.secret_key='DUIJSF98RDBFnsjeurndp'
    app.config["SESSION_PERMANENT"]= False
    app.config["SESSION_TYPE"] = "filesystem"




    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
