"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from wtforms import Form, StringField, IntegerField, PasswordField

from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

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