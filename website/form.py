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
    name = StringField('Nome', validators=[DataRequired()])
    surname = StringField('Cognome', validators=[DataRequired()])
    street = StringField('Via' , validators=[DataRequired()])
    city = StringField('Città',validators=[DataRequired()])
    province = StringField('Provincia',validators=[DataRequired()])
    date = StringField('Data di nascita',validators=[DataRequired()])
    gender = RadioField('Genere', choices=[('M'),('F')], validators=[DataRequired()])
    telephone = StringField('Numero di telefono',validators=[DataRequired()])
    taxcode = StringField('Codice fiscale',validators=[DataRequired()])
    submit = SubmitField('Registrati',validators=[DataRequired()])


class RiderSigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password ', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    surname = StringField('Cognome', validators=[DataRequired()])
    street = StringField('Via' , validators=[DataRequired()])
    city = StringField('Città',validators=[DataRequired()])
    province = StringField('Provincia',validators=[DataRequired()])
    date = StringField('Data di nascita',validators=[DataRequired()])
    gender = RadioField('Genere', choices=[('M'),('F')], validators=[DataRequired()])
    telephone = StringField('Numero di telefono',validators=[DataRequired()])
    taxcode = StringField('Codice fiscale',validators=[DataRequired()])
    submit = SubmitField('Registrati',validators=[DataRequired()])
    id = StringField('Numero carta identità',validators=[DataRequired()])
    iban = StringField('Iban',validators=[DataRequired()])

class LocalSigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password ', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    surname = StringField('Cognome', validators=[DataRequired()])
    street = StringField('Via' , validators=[DataRequired()])
    city = StringField('Città',validators=[DataRequired()])
    province = StringField('Provincia',validators=[DataRequired()])
    date = StringField('Data di nascita',validators=[DataRequired()])
    gender = RadioField('Genere', choices=[('M'),('F')], validators=[DataRequired()])
    telephone = StringField('Numero di telefono',validators=[DataRequired()])
    taxcode = StringField('Codice fiscale',validators=[DataRequired()])
    submit = SubmitField('Registrati',validators=[DataRequired()])
    id = StringField('Numero carta identità',validators=[DataRequired()])
    iban = StringField('Iban',validators=[DataRequired()])
    localname = StringField('Nome del locale',validators=[DataRequired()])
    piva = StringField('Piva',validators=[DataRequired()])


class EditProfile(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password ', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    surname = StringField('Cognome', validators=[DataRequired()])
    street = StringField('Via' , validators=[DataRequired()])
    city = StringField('Città',validators=[DataRequired()])
    province = StringField('Provincia',validators=[DataRequired()])
    date = StringField('Data di nascita',validators=[DataRequired()])
    gender = RadioField('Genere', choices=[('M'),('F')], validators=[DataRequired()])
    telephone = StringField('Numero di telefono',validators=[DataRequired()])
    taxcode = StringField('Codice fiscale',validators=[DataRequired()])
    submit = SubmitField('Aggiorna',validators=[DataRequired()])
    id = StringField('Numero carta identità',validators=[DataRequired()])
    iban = StringField('Iban',validators=[DataRequired()])
    localname = StringField('Nome del locale',validators=[DataRequired()])
    piva = StringField('Piva',validators=[DataRequired()])