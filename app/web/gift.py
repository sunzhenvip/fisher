from . import web

__author__ = '七月'

from flask_login import login_required, current_user
from ..models.base import db
from ..models.gift import Gift
from flask import current_app


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    # can_save_to_list()
    # if current_user.can_save_to_list(isbn):
    current_user.can_save_to_list()
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    # current_user.beans += 0.5
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
