import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from src.database import prepare_database, get_db
from src.main import app
from src.settings import Settings

TEST_DB_URL = 'postgres://postgres@localhost:5432/dungeonfinder_test'
settings = Settings(database_url=os.getenv('DATABASE_URL', TEST_DB_URL))

engine = prepare_database(delete_existing=True, settings=settings)


def override_get_db():
    db = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(settings.database_url))
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
test_client = TestClient(app)
