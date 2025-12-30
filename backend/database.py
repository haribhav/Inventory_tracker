from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url ="postgresql://postgres:admin123@localhost:5432/Python_DB_fastApi"

engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush = False, bind = engine)
