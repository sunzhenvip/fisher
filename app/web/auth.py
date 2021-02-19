from . import web

__author__ = 'sz'

from flask import render_template, request, redirect, url_for, flash, request

from ..forms.auth import RegisterForm, LoginForm, EmailForm
from ..models.base import db
from ..models.user import User
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # print(form.validate())
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            print(form.data)
            user.set_attrs(form.data)
            db.session.add(user)
            # db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            # print(next)
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form={'data': {}})
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            try:
                user = User.query.filter_by(email=account_email).first_or_404()
            except Exception as e:
                return render_template('404.html')
            from app.libs.email import send_mail
            send_mail(form.email.data, '重置密码', 'email/reset_password.html', user=user, token='231234454')

    return render_template('auth/forget_password_request.html', form=form)
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
