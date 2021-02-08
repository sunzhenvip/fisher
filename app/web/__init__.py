"""
 Created by sz on 2021/2/4
"""
from flask import Blueprint

__author__ = 'sz'

web = Blueprint('web', __name__)

from app.web import book
# from app.web import user
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
