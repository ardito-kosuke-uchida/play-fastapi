from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Model


class Post(Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String)
    body = Column(String)
    account_id = Column(Integer, ForeignKey("account.id"))
    account = relationship("Account")
