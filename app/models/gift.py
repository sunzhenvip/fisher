"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from flask import current_app

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship
from collections import namedtuple
from app.spider.yushu_book import YuShuBook

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    __tablename__ = 'gift'
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        # 根据传入的一组isbn，到gift 表中检索出相应的礼物 并且计算出某个礼物
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        # 对象 | 字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # status = Column(SmallInteger, )
    # 类方法
    @classmethod
    def recent(cls):
        # 链式调用
        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn
        ).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
