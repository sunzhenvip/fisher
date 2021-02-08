"""
 Created by sz on 2021/2/3
"""

from app.libs.httper import HTTP
from flask import current_app

__author__ = 'sz'


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []
        # self.to

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        # sys.exit(0)
        result = HTTP.get(url)
        self.__fill_single(result)
        # print(result);
        # 结果是 dict
        # url = self.isbn_url
        # return result

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, count=15, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return result

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
