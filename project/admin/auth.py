from flask import Blueprint, render_template

auth = Blueprint('auth_admin', __name__, url_prefix='/admin')


@auth.route('/login')
def login():
    return render_template('admin/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    return "aeeeee"


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