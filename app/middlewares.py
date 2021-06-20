import traceback

from fastapi import Request, Response, status
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware

from app.database import Session


def setup(app):

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
        ],
    )

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        """ リクエストごとにSQLAlchemy Session オブジェクトを作成"""
        request.state.db_session = Session()
        try:
            response = await call_next(request)
            request.state.db_session.commit()
        except Exception:
            logger.error(traceback.format_exc())
            request.state.db_session.rollback()
            response = Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            request.state.db_session.close()
        return response
