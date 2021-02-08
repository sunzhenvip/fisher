"""
 Created by sz on 2021/2/8
"""
__author__ = 'sz'

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # gifts = relationship('Gift')
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    _password = Column('password', String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, row):
        self._password = generate_password_hash(row)
