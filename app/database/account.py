from sqlalchemy import Column, Integer, String

from .database import Model


class Account(Model):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
