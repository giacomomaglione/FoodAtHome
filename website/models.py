from . import login
from . import cliente
from flask_wtf import FlaskForm
from flask_login import LoginManager
class Cliente():
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @login.user_loader
    def load_user(username):
        u = cliente.find_one({"Name": username})
        if not u:
            return None
        return cliente(username=u['username'])



class Rider():
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @login.user_loader
    def load_user(username):
        u = cliente.find_one({"Name": username})
        if not u:
            return None
        return cliente(username=u['username'])