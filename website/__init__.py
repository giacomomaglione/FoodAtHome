from flask import Flask
from pymongo import MongoClient
import certifi
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BNRD gnmldesw HUgI HSNsgs'


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
