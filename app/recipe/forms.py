from flask_wtf import FlaskForm
from wtforms import TextField, StringField
from wtforms.validators import DataRequired, Email, Length
from ..models import Category, Recipe

class Categoryform(FlaskForm):
    name = TextField('name', validators = [DataRequired(),Length(min=6, max=30)])
    description = StringField('description', validators = [DataRequired(), Length(min=6, max=500)])
	
class Recipeform(FlaskForm):
    name = TextField('name', validators = [DataRequired(), Length(min=6, max=30)])
    description = StringField('description', validators = [DataRequired(), Length(min=6, max=500)])