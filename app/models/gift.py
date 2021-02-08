"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship


class Gift(Base):
    __tablename__ = 'gift'
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    # status = Column(SmallInteger, )
