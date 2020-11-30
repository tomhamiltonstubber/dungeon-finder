import logging
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


logger = logging.getLogger('df')


def session_local(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def prepare_database(delete_existing: Union[bool, callable], settings):
    """
    (Re)create a fresh database and run migrations.

    :param delete_existing: whether or not to drop an existing database if it exists
    :return: whether or not a database as (re)created
    """
    engine = create_engine(settings.database_url)
    if delete_existing:
        try:
            logger.info('Wiping database...')
            Base.metadata.drop_all(engine)
        except OperationalError:
            raise RuntimeError('Database not yet created. Run `make reset-test-db` to create it.')
    logger.info('Creating database...')
    Base.metadata.create_all(engine)


def get_db():
    from main import settings
    db = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(settings.database_url))
    try:
        yield db
    finally:
        db.close()
