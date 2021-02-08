"""
 Created by sz on 2021/2/3
"""
import json

from flask import jsonify, request, render_template
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
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }
    # print(r)
    return render_template('test.html', data=r)
