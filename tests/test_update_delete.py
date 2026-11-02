from cisc217_week11.database import (
    add_character, delete_character, get_character, update_health,
)


def test_update_health(session):
    hero = add_character(session, "Aria", 100, 85)
    assert update_health(session, hero.id, 72) is True
    assert get_character(session, hero.id).health == 72


def test_update_health_missing(session):
    assert update_health(session, 9999, 72) is False


def test_delete_character(session):
    hero = add_character(session, "Aria", 100, 85)
    assert delete_character(session, hero.id) is True
    assert get_character(session, hero.id) is None


def test_delete_missing(session):
    assert delete_character(session, 9999) is False
