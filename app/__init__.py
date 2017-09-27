from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


##config##
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)
app.config.from_object('config.Developer')

yummy = SQLAlchemy(app)

#setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = 'You must be logged in to view this'
login_manager.view='user.login'

from app import models

from .user import user as user_blueprint
from .recipe import recipe as recipe_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)