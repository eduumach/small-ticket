from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('user/profile.html', name=current_user.name)


@main.route('/admin')
def admin():
    return render_template('admin/index.html')
