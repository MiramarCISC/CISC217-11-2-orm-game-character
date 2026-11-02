from cisc217_week11.database import (
    add_character, add_character_type, characters_by_type,
    get_character, list_characters, strong_characters,
)


def seed(session):
    mage = add_character_type(session, "Mage")
    warrior = add_character_type(session, "Warrior")
    aria = add_character(session, "Aria", 100, 85, mage)
    borin = add_character(session, "Borin", 120, 70, warrior)
    cyra = add_character(session, "Cyra", 90, 95, mage)
    return aria, borin, cyra


def test_get_character(session):
    aria, _, _ = seed(session)
    assert get_character(session, aria.id) is aria


def test_get_character_missing(session):
    assert get_character(session, 9999) is None


def test_list_characters_orders_by_id(session):
    aria, borin, cyra = seed(session)
    result = list_characters(session)
    assert [c.id for c in result] == [aria.id, borin.id, cyra.id]


def test_strong_characters_filters_and_sorts(session):
    seed(session)
    assert [c.name for c in strong_characters(session, 80)] == ["Cyra", "Aria"]


def test_characters_by_type(session):
    seed(session)
    assert [c.name for c in characters_by_type(session, "Mage")] == ["Aria", "Cyra"]


def test_unknown_type_returns_empty_list(session):
    seed(session)
    assert characters_by_type(session, "Rogue") == []
