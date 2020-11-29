from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import Settings

Base = declarative_base()
engine = create_engine(Settings().database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
