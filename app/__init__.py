from flask import Flask


app = Flask(__name__)



from app import models

from .user import user as user_blueprint
from .recipe import recipe as recipe_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)