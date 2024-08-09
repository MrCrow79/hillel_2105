from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:123@localhost/postgres"
DATABASE_URL2 = r"sqlite:///D:\hillel\pythonProject\hillel_2105\lessons\lesson_20\my_sqlite3.db"





engine = create_engine(DATABASE_URL2)

Base = declarative_base()