import os

from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DB_HOST: str = os.environ.get("DB_HOST")
DB_ROOT: str = os.environ.get("DB_ROOT")
DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
DB_NAME: str = os.environ.get("DB_NAME")
