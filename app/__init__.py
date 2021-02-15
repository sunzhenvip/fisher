"""
 Created by sz on 2021/2/4
"""
from flask import Flask
from flask_login import LoginManager
from app.models.base import db

__author__ = 'sz'

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_buleprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登陆或注册'

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app


# 注册蓝图
def register_buleprint(app):
    from app.web.book import web
    # from app.web.user import user
    app.register_blueprint(web)
    # app.register_blueprint(user)
