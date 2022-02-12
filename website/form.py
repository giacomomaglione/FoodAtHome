from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField, DateField, IntegerField
from wtforms.validators import DataRequired, InputRequired

form = Blueprint('form', __name__)

class Login(FlaskForm):
    email = StringField('Indirizzo Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ClientSigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password ', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    street = StringField('Street' , validators=[DataRequired()])
    city = StringField('City',validators=[DataRequired()])
    province = StringField('Province',validators=[DataRequired()])
    date = DateField('Date',validators=[DataRequired()])
    gender = RadioField('Gender', validators=[DataRequired()])
    telephone = IntegerField('Telephone',validators=[DataRequired()])
    taxcode = IntegerField('Taxcode',validators=[DataRequired()])
    submit = SubmitField('Registrati',validators=[DataRequired()])

