from flask_wtf import FlaskForm
from wtforms import TextField, StringField
from wtforms.validators import DataRequired, Length
from ..models import User

class Categoryform(FlaskForm):
    category_name = TextField('name', validators = [DataRequired(),Length(min=6, max=30)])
    category_description = StringField('description', validators = [DataRequired(), Length(min=6, max=500)])
	
class Recipeform(FlaskForm):
    recipe_name = TextField('name', validators = [DataRequired(), Length(min=6, max=30)])
    recipe_description = StringField('description', validators = [DataRequired(), Length(min=6, max=500)])
