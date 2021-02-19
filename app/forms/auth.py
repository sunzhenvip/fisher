"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from wtforms import Form, StringField, IntegerField, PasswordField

from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(5, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空,请输入密码'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='至少两个字符昵称,最多10个字符昵称')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已经被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(5, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空,请输入密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规则')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[DataRequired('密码不能为空，请输入密码'), Length(6, 32, message='密码长度需要在6到32位之间'),
                                          EqualTo('password2', message='两次输入的密码不一致')])
    password1 = PasswordField(validators=[DataRequired('确认密码不能为空，请输入密码'), Length(6, 32, message='确认密码长度需要在6到32位之间')])
