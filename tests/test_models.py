from sqlalchemy import inspect
from cisc217_week11.models import Character, CharacterType


def test_character_type_table_name():
    assert CharacterType.__tablename__ == "character_types"


def test_character_table_name():
    assert Character.__tablename__ == "characters"


def test_character_type_columns():
    mapper = inspect(CharacterType)
    assert set(mapper.columns.keys()) == {"id", "name"}
    assert mapper.columns.id.primary_key is True
    assert mapper.columns.name.nullable is False


def test_character_columns():
    mapper = inspect(Character)
    assert set(mapper.columns.keys()) == {"id", "name", "health", "power", "type_id"}
    assert mapper.columns.id.primary_key is True
    assert mapper.columns.name.nullable is False
    assert mapper.columns.health.nullable is False
    assert mapper.columns.power.nullable is False
    assert mapper.columns.type_id.nullable is True
