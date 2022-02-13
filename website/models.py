from . import login
from . import cliente
from flask_wtf import FlaskForm
from flask_login import LoginManager

class Cliente():
    def __init__(self, Email, type):
        self.Email = Email
        self.type = type

    @staticmethod
    def is_authenticated(self):
        return True

    @staticmethod
    def is_active(self):
        return True

    @staticmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.Email


class Rider():
    def __init__(self, Email, type):
        self.Email = Email
        self.type = type
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
        return self.Email


class Local():
    def __init__(self, Email, type):
        self.Email = Email
        self.type = type
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
        return self.Email