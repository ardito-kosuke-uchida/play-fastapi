from .repository_base import RepositoryBase
from app import models
from app import database as db


class PostRepository(RepositoryBase):

    def create(self, post_in: models.PostIn, account: db.Account):
        post = db.Post(**dict(post_in), account=account)
        self._session.add(post)
        self._session.flush()
        return post

    def get(self, post_id):
        return self._session.query(db.Post).get(post_id)

    def list_item(self, limit, offset):
        return self._session.query(db.Post).limit(limit).offset(offset).all()
