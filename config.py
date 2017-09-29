"""config for different environments"""
import os
from app import app
from flask_wtf.csrf import CSRFProtect
#define directory for application
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """config super class"""
    DEBUGING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///'\
    +os.path.join(BASEDIR, 'yummy_db')
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Xmas1945Mars'
	
class Developer(Config): 
    """for development purposes"""
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'\
    +os.path.join(BASEDIR, ':memory:')
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_SECRET_KEY = 'XMAS1945mars'
    csrf = CSRFProtect(app)
