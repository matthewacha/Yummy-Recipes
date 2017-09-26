from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from app import yummy, login_manager


class User(yummy.Model, UserMixin):
    __tablename__ = 'user'
    id = yummy.Column(yummy.Integer, primary_key=True)
    first_name = yummy.Column(yummy.String(60))
    last_name = yummy.Column(yummy.String(60))
    email = yummy.Column(yummy.String(60), unique=True)
    password_hash = yummy.Column(yummy.String(300))
    category_id = yummy.Column(yummy.Integer, yummy.ForeignKey('categories.id'))
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    @property
    def password(self):
        #keep password private
        raise AttributeError('password is not a readable attribute.')  
   
    @password.setter  
    def password(self, password):
       #generate password_hash
        self.password_hash = generate_password_hash(password) 
		
    def verify_password(self, password):
        #check password with password_hash
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '{}'.format(self.first_name)
  
    #setup user loader  
    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))
 
class Category(yummy.Model):
    __tablename__ = 'categories'
    id = yummy.Column(yummy.Integer, primary_key=True)
    name = yummy.Column(yummy.String(60), nullable=False)
    description = yummy.Column(yummy.String(200), nullable=False)
    recipe_id=yummy.Column(yummy.Integer, ForeignKey('recipies.id'))
    user = yummy.relationship('User', backref='categories',
                                 lazy='dynamic')
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return '{} {}'.format(self.name, self.description)
		
class Recipe(yummy.Model):
    __tablename__ = 'recipies'	
    id = yummy.Column(yummy.Integer, primary_key=True)
    name = yummy.Column(yummy.String(100), nullable=False)
    description = yummy.Column(yummy.String(500), nullable=False)
    category = yummy.relationship('Category', backref='recipes', \
	                               lazy='dynamic')
    def __init__(self, name, description):
        self.name = name 
        self.description = description
    def __repr__(self):
        return '{}'.format(self.name)	

    #create engine to store data in local database directory   

shoppers.Model.metadata.bind = create_engine('sqlite:///yummy.db') 

shoppers.create_all