from sqlalchemy import inspect

from cisc217_week11.database import add_character, add_character_type
from cisc217_week11.models import Character, CharacterType


def test_character_type_has_characters_relationship():
    assert "characters" in inspect(CharacterType).relationships


def test_character_has_character_type_relationship():
    assert "character_type" in inspect(Character).relationships


def test_relationship_is_bidirectional(session):
    mage = add_character_type(session, "Mage")
    aria = add_character(session, "Aria", 100, 85, mage)
    cyra = add_character(session, "Cyra", 90, 95, mage)

    assert aria.character_type is mage
    assert cyra.character_type is mage
    assert [c.name for c in mage.characters] == ["Aria", "Cyra"]


def test_character_type_foreign_key():
    mapper = inspect(Character)
    foreign_keys = mapper.columns.type_id.foreign_keys
    assert len(foreign_keys) == 1
    foreign_key = next(iter(foreign_keys))
    assert foreign_key.target_fullname == "character_types.id"
