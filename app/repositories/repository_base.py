from app.database import Session
from fastapi import Depends
from app.dependencies import db_session


class RepositoryBase:

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session
