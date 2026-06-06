from flask import  render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.auth import auth

from app.extensions import db
from app.models import User
from app.auth.forms import RegisterForm, LoginForm



@auth.route('/')
def home():
    return render_template('index.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        existing_email = User.query.filter_by(email=form.email.data).first()

        if existing_email:
            flash('Email already exists', 'error')
            return redirect(url_for('auth.register'))

        user = User(
            pf_number=form.pf_number.data,
            full_name=form.full_name.data,
            email=form.email.data
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Await admin approval.', 'success')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):

            if not user.approved:
                flash('Account awaiting admin approval', 'error')
                return redirect(url_for('auth.login'))

            login_user(user)

            if user.role == 'admin':
                return redirect(url_for('admin.dashboard'))

            return redirect(url_for('member.dashboard'))

        flash('Invalid credentials', 'error')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('auth.login'))