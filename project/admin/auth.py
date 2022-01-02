from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from models import Admin

auth = Blueprint('auth_admin', __name__, url_prefix='/admin')


@auth.route('/login')
def login():
    return render_template('admin/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    admin = Admin.query.filter_by(email=email).first()

    if not admin or not check_password_hash(admin.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_user.login'))

    login_user(admin, remember=remember)
    return redirect(url_for('main.profile'))
    

@auth.route('/signup')
def signup():
    return "aeeeee"


@auth.route('/signup', methods=['POST'])
def signup_post():
    return "aeeee"


@auth.route('/logout')
#@login_required
def logout():
    return "aeee"