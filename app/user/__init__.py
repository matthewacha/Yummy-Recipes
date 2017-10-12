from flask import Flask, Blueprint

user = Blueprint('user', __name__, template_folder = 'templates')

from . import views

__all__ = ['user']
