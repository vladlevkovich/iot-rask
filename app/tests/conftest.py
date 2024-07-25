import pytest
from app.models.models import *


@pytest.fixture(scope='function')
def test_db():
    test_db = SqliteDatabase(':memory:')
    MODELS = [User, Location, Device]
    test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
    test_db.connect()
    test_db.create_tables(MODELS)
    yield test_db
    test_db.drop_tables(MODELS)
    test_db.close()

