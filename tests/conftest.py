import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from cisc217_week11.database import create_schema


@pytest.fixture
def engine():
    engine = create_engine("sqlite:///:memory:")
    create_schema(engine)
    return engine


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session
