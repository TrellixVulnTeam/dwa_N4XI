from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,IntegerField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange
from app.models import User,Specijalizacija,Bolnica
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Zapamti')
    submit = SubmitField('Prijava')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Ponovi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registriraj se')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class Ocjeni_doktoraForm(FlaskForm):
    ocjena = IntegerField('Ocjena (1-5)', validators=[DataRequired(),NumberRange(min=1, max=5, message='Unesi ocjenu(1-5)')])
    opis = TextAreaField('Opis', validators=[DataRequired()])
    submit = SubmitField('Dodaj')