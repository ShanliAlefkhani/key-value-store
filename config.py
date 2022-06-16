from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_password: str
    redis_db: int

    url: str

    class Config:
        env_file = ".env"
