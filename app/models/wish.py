"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from app.spider.yushu_book import YuShuBook
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base


class Wish(Base):
    __tablename__ = 'wish'
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    # status = Column(SmallInteger, )

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book
