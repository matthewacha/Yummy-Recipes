from flask import render_template, flash, redirect, url_for, request, Blueprint,session
import forms
from forms import Registerform, Loginform
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

user = Blueprint('user', __name__, template_folder = 'templates')

all_users=[]

def login_required(fx):
    @wraps(fx)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return fx(*args, **kwargs)
        else:
            flash('You need to be logged in')
            return redirect(url_for('user.login'))
    return wrap

@user.route('/')
def index():
    return redirect(url_for('user.register'))

@user.route('/signup', methods=['GET','POST'])
def register():
    form = Registerform()
    if request.method == 'POST':
        try:
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = generate_password_hash(form.password.data)
            user = {
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password':password,
                'recipes':[]

                }
            all_users.append(user)
            flash('Congratulations, login to confirm your account')
            return redirect(url_for('user.login'))
        except:
            flash('Error please try again')
            pass
        return redirect(url_for('user.register'))
    return render_template('register.html', title = 'Signup',
                           form = form)
   
@user.route('/login', methods = ['GET', 'POST'])
def login():
    form = Loginform()
    if request.method == 'POST':
        for user in all_users:
            for key in user.keys():
                if user['email'] == form.email.data:
                    passwordh = user['password']
                    if check_password_hash(passwordh, form.password.data):
                        session['logged_in']=True
                        session['current_user']=form.email.data
                        flash('Welcome')
                        return redirect(url_for('recipe.list_recipes'))
                flash('Wrong email')
                redirect(url_for('user.login'))
    return render_template('login.html', tilte='Login', form = form)

@user.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('current_user', None)
    flash('You must login again')
    return redirect(url_for('user.login'))
