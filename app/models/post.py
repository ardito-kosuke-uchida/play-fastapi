from pydantic import BaseModel
from .account import Account


class Post(BaseModel):
    id: int
    subject: str
    body: str

    account: Account

    class Config:
        orm_mode = True


class PostIn(BaseModel):
    subject: str
    body: str
