from pydantic import BaseSettings


class Settings(BaseSettings):

    stage: str = "development"
    sqlalchemy_database_uri: str = None

    class Config:
        env_file = ".env"
