from pydantic import BaseSettings,Field
from dotenv import load_dotenv

from pathlib import Path
load_dotenv()
class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    MONGO_INITDB_DATABASE: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
         env_file = '.env'
         env_prefix = ""
         case_sentive = False

settings = Settings('')

