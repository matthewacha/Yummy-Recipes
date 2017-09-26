from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from app.user.forms import Registerform, Loginform
from app import csrf

from app import yummy
from ..models import User
from . import user

@user.route('/signup', methods=['GET','POST'])
def register():
    form = Registerform(request.form)
    if request.method == 'POST':
        if form.validate():
            fname = form.first_name.data
            lname = form.last_name.data
            mail = form.email.data
            pasword = form.password.data
            new_user = User(fname, lname, mail, pasword)
            yummy.session.add(new_user)
            yummy.session.commit()
            flash('Congratulations,login to confirm your account')
            return redirect(url_for('user.login'))
        flash('Sorry,wrong email or password')
        print form.errors
        return redirect(url_for('user.register'))		
    return render_template('register.html', title = 'Signup', form = form, csrf_token=csrf)
   
@user.route('/login', methods = ['GET', 'POST'])
def login():
    form = Loginform()
    if request.method == 'POST':
        if form.validate():
            n_user = User.query.fetch_all(email = form.email.data).first()
            if nuser is not None:
                if User.verify_password(form.password.data):
			        login_user(n_user)
			        flash('Welcome!!')
			        return redirect(url_for('recipe.dashboard'))
                flash('Wrong password')	
                return redirect(url_for('user.login'))
            flash('Wrong password')
        print form.errors	
        return redirect(url_for('user.login'))	
    return render_template('login.html', tilte='Login', form = form)

@user.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('user.login')