from . import web

__author__ = 'sz'

from flask import render_template, request

from ..forms.auth import RegisterForm
from ..models.base import db
from ..models.user import User
from werkzeug.security import generate_password_hash


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # print(form.validate())
    if request.method == 'POST' and form.validate():
        user = User()
        print(form.data)
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        pass
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
