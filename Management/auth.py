from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required,logout_user
from .models import User
from . import db


#create a blueprintfrom .models import User
bp = Blueprint('auth', __name__)


# this is the hint for a login function
@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        emailid = login_form.emailid.data
        password = login_form.password.data
        u1 = User.query.filter_by(emailid=emailid).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect Email Address'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('login.html', form=login_form, heading='Login')


# this is the hint for a register function
@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    #the validation of form submis is fine
    if (register.validate_on_submit() == True):
            #get username, password and email from the form
            username =register.userName.data
            password = register.password.data
            confirm = register.confirm.data
            email = register.emailid.data
            contact = register.contactNumber.data
            address = register.address.data
            #check if a user exists
            u1 = User.query.filter_by(emailid=email).first()
            if u1:
                flash('Email Address already exists in the database. Please Log In.')
                return redirect(url_for('auth.login'))
            if password != confirm:
                flash('Password and Password Confirmation Inputs do not match. Please Re-Input Data.')
                return redirect(url_for('auth.register'))
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(password)
            #create a new user model object
            new_user = User(userName=username, password_hash=pwd_hash, emailid=email, contactNumber=contact, address=address )
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            return redirect(url_for('auth.login'))
    #the else is called when there is a get message
    else:
        return render_template('register.html', form=register, heading='Register')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))