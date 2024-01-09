from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

connection_string = os.getenv("DATABASE_URL")
engine = create_engine(connection_string)
sessionlocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)
Base = declarative_base 

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
