from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from app.user.forms import Registerform, Loginform

from app import yummy
from ..models import User
from . import user

@user.route('/signup', methods=['GET','POST'])
def register():
    form = Registerform()
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
        return redirect(url_for(user.register))		
    return render_template('register.html', title = 'Signup', form = form)
   
@user.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html', tilte='Login')

"""@user.logout('/logout', methods = ['GET','POST'])
def logout():
    return render_template('register.html')"""