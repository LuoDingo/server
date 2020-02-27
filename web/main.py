from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from . import events

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/chatroom')
@login_required
def session():
    return render_template('chatroom.html', is_authenticated=current_user.is_authenticated)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


