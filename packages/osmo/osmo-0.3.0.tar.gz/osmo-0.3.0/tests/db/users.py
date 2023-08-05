# -*- coding:utf-8 -*-

from sqlalchemy import (
    Column,
    Integer,
    String
)

from base import BASE


class UserModel(BASE):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
