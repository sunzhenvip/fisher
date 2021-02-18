from . import web

__author__ = '七月'

from ..models.gift import Gift
from ..view_model.book import BookViewModel
from flask import render_template


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    print(recent_gifts)
    print(123)
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
