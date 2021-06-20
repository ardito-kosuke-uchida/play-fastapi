from .repository_base import RepositoryBase
from app import models
from app import database as db
import hashlib


class AccountRepository(RepositoryBase):

    def create(self, account_in: models.AccountIn):
        account = db.Account(**{
            **dict(account_in),
            "password": hashlib.sha256(account_in.password.encode("utf8")).hexdigest(),
        })
        self._session.add(account)
        self._session.flush()
        return account

    def get(self, account_id):
        return self._session.query(db.Account).get(account_id)

    def patch(self, account: db.Account, account_patch: models.AccountPatch):
        for k, v in dict(account_patch).items():
            setattr(account, k, v)

        self._session.flush()
        return account
