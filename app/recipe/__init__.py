from flask import Flask, Blueprint

recipe = Blueprint('recipe', __name__, template_folder = 'templates')

from . import views