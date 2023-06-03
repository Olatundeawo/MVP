from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required

from project.models.users import User

from . extensions import db, bcrypt

auth = Blueprint('auth', __name__)
#bcrypt = Bcrypt(auth)


@auth.route('/login')
def login():
    
    return (render_template('login.html'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('passsword')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()

    # check if the user exists by taking the 
    # the password, hash it and compare it with the hashed one saved
    if not user or not bcrypt.check_password_hash(user.password, password):
    #if not user or not user.password:
        flash('Email or Password supplied is not correct')
        return (redirect(url_for('auth.login')))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))




@auth.route('/signup')
def signup():
    return (render_template('signup.html'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    # check if email already exist
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email already used')
        return (redirect(url_for('auth.signup')))

    # Create a new user hash the password no to store it in a plain text
    #new_user = User(email=email, name=name, password=password)
    new_user = User(email=email, name=name, password=bcrypt.generate_password_hash(password).decode('utf-8'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return (redirect(url_for('auth.login')))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return (redirect(url_for('main.index')))

