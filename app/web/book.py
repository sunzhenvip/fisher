"""
 Created by sz on 2021/2/3
"""
import json

from flask import jsonify, request, render_template
from flask_login import current_user

from app.forms.book import SearchFrom
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_model.book import BookViewModel, BookCollection
from . import web

# import json

__author__ = 'sz'

# app = Flask(__name__)

# @app.route('/index')
# def index():
#     return '1212'

# @web.route('test')
# def test():
#     return '1212'

# 蓝图 分文件
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_model.trade import TradeInfo


@web.route('/book/search')
def search():
    """
        q:普通关键字搜索 , isbn 搜索
        start
    """
    # q = request.args['q']
    # page = request.args['page']
    # 验证器
    form = SearchFrom(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # q print(page)
        isbn_or_key = is_isbn_or_key(q)
        # print(page)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)

            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.pacage_single(result, q)
        else:
            yushu_book.search_by_keyword(q)

            # result = YuShuBook.search_by_keyword(q)
            # result = BookViewModel.pacage_collection(result, q)
        # 难用写法
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        # flask 简写写法 返回json格式数据
        books.fill(yushu_book, q)
        # print(books)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
        # return jsonify(result)
        # print(books)
        return render_template('search_result.html', books=books)
    else:
        return render_template('search_result.html', books=books)
        # return jsonify(form.errors)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True

        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes,
                           )


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }
    # print(r)
    return render_template('test.html', data=r)
