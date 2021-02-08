"""
 Created by sz on 2021/2/7
"""
__author__ = 'sz'


# from os.path import join
class BookViewModel:
    def __init__(self, yushu_book):
        self.title = yushu_book['title']
        self.publisher = yushu_book['publisher']
        self.author = '、'.join(yushu_book['author'])
        self.image = yushu_book['image']
        self.price = yushu_book['price']
        self.summary = yushu_book['summary']
        self.isbn = yushu_book['isbn']
        self.pages = yushu_book['pages']

    # 访问可以不需要加方法名称 例如 对象.intro
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [
            self.author,
            self.publisher,
            self.price
        ])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    @classmethod
    def pacage_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def pacage_collection(cls, data, keyword):
        print(keyword)
        returned = {
            'books': [],
            'total': data['total'],
            'keyword': keyword
        }
        print(returned)
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return data

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image']
        }
        return book

# 播放7-3节
