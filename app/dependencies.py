from fastapi import Request, Depends, HTTPException, status
from fastapi.security.http import HTTPBasic, HTTPBasicCredentials
from app import database as db
import hashlib


def db_session(request: Request):
    """ SQLAlchemy Sessionオブジェクト"""
    return request.state.db_session


def basicauth(
    request: Request,
    cred: HTTPBasicCredentials = Depends(HTTPBasic()),
    session=Depends(db_session),
):
    """ Basic認証 """
    account = (
        session.query(db.Account)
        .filter(
            db.Account.email == cred.username,
            db.Account.password == hashlib.sha256(cred.password.encode("utf8")).hexdigest(),
        )
        .first()
    )

    if account is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    request.state.account = account


def currentuser(request: Request):
    """ ログインユーザー"""
    return request.state.account

def pagination_params(limit: int = 10, offset: int = 0):
    return {
        "limit": limit,
        "offset": offset,
    }
