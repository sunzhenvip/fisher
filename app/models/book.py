"""
 Created by sz on 2021/2/6
"""

from sqlalchemy import Column, Integer, String
from app.models.base import Base

__author__ = 'sz'


class Book(Base):
    __tablename__ = 'book'
    # 整形，唯一自增长，
    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    title = Column(String(50), nullable=False, default='1212', comment='标题')
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
