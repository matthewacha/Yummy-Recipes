from flask_wtf import FlaskForm
from wtforms import TextField, StringField
from wtforms.validators import DataRequired, Email, Length

class Registerform(FlaskForm):
    first_name = TextField('first_name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = TextField('last_name', validators=[DataRequired(), Length(min=1, max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(min=6, max=60)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=60)])

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=60)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=60)])
 

