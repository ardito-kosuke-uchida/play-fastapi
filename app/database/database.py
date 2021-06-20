from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import Settings

settings = Settings()

engine = create_engine(settings.sqlalchemy_database_uri, echo=True, pool_size=20)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Model = declarative_base()
