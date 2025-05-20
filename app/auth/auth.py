from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user
from ..models import User
from .. import db, login_manager

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Usuario o contraseña inválidos')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
