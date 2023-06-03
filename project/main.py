from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . extensions import db, bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return (render_template('index.html'))

@main.route('/profile')
@login_required
def profile():
    #return (render_template('profile.html'))
    return (render_template('context.html', name=current_user.name))
 #name=current_user.name
