"""
 Created by sz on 2021/2/4
"""
from flask import Flask
from app.models.base import db

__author__ = 'sz'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_buleprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


# 注册蓝图
def register_buleprint(app):
    from app.web.book import web
    # from app.web.user import user
    app.register_blueprint(web)
    # app.register_blueprint(user)
