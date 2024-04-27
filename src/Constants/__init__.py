import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    KNOWN_HOST = os.environ.get("KNOWN_HOST")
    PORT = os.environ.get("PORT")
