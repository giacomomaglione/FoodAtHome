from flask import Flask
from website import database
#from flask_pymongo import PyMongo
#from pymongo import MongoClient
#import certifi
from flask_login import LoginManager

#connessione = MongoClient("mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test", tlsCAFile=certifi.where())
#database = connessione["foodathome"]

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BNRD gnmldesw HUgI HSNsgs'
    database.Database.initialize()
    #connessione.init_app(app)

    #connessione = PyMongo(app, uri="mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test", tlsCAFile=certifi.where())
    #connessione = MongoClient("mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test", tlsCAFile=certifi.where())
    #database = connessione["foodathome"]
    #database = connessione.db
    #cliente = database["Customer"]
    #rider = database["Rider"]
    #negozio = database["Store"]

    # login_manager= LoginManager()
   # login_manager.login_view = 'auth.login'
   # login_manager.init_app(app)

   # @login_manager.user_loader
   # def load_user(id):
   #     user = cliente.find_one({"id": id})
   # return user

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
