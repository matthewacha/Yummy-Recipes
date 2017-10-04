from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_required, login_user, logout_user
from app.user.forms import Registerform, Loginform

from app.user import forms
from forms import Registerform, Loginform
from app import yummy, app
from . import user

class User(object):
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
all_users = []
@user.route('/signup', methods=['GET','POST'])
def register():
    form = Registerform()
    if request.method == 'POST':
        try:
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            new_user = User(first_name, last_name, email, password)
            all_users.append(new_user)
            flash('Congratulations, login to confirm your account')
            return redirect(url_for('user.login'))
        except:
            flash('Sorry,wrong email or password')
            print form.errors
        return redirect(url_for('user.register'))
    return render_template('register.html', title = 'Signup',
                           form = form)
   
@user.route('/login', methods = ['GET', 'POST'])
def login():
    form = Loginform()
    if request.method == 'POST':
        for user in all_users:
            if user.email == form.email.data:
                if user.password == form.password.data:
                    session['logged_in'] = True
                    return redirect(url_for('recipe.list_categories'))
                flash('Wrong password')
            flash('Wrong email')
            flash(user.email)
            return redirect(url_for('user.login'))
    return render_template('login.html', tilte='Login', form = form)

@user.route('/logout', methods = ['GET','POST'])
def logout():
    if session['logged_in'] == True:
        session.clear()
        flash('Login to resume')
        return render_template('user.login')
    return render_template('user.login')
