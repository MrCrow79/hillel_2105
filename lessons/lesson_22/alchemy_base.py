from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = "postgresql://postgres:123@localhost/postgres"
import pathlib

BASE_PATH = str(pathlib.Path(__file__).parent)
DATABASE_URL2 = rf"sqlite:///{BASE_PATH}/my_sqlite3.db"





engine = create_engine(DATABASE_URL2)

Base = declarative_base()