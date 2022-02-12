from flask import Flask
from website import database
from flask_login import LoginManager

database.Database.initialize()

cliente = database.Database.DATABASE["Customer"]
rider = database.Database.DATABASE["Rider"]
negozio = database.Database.DATABASE["Store"]

login = LoginManager()
login.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BNRD gnmldesw HUgI HSNsgs'
    app.secret_key ='DUIJSF98RDBFnsjeurndp'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    from .views import views
    from .auth import auth
    from .form import form

    login.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(form, url_prefix='/')

    return app
