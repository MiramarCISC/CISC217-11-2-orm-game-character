from cisc217_week11.database import add_character, add_character_type
from cisc217_week11.models import Character, CharacterType


def test_add_character_type(session):
    mage = add_character_type(session, "Mage")
    assert isinstance(mage, CharacterType)
    assert mage.id is not None
    assert mage.name == "Mage"


def test_add_character(session):
    hero = add_character(session, "Aria", 100, 85)
    assert isinstance(hero, Character)
    assert hero.id is not None
    assert hero.character_type is None


def test_add_character_with_type(session):
    mage = add_character_type(session, "Mage")
    hero = add_character(session, "Aria", 100, 85, mage)
    assert hero.character_type is mage
    assert hero.type_id == mage.id
