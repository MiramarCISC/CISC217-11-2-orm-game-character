"""Database operations for the Week 11 SQLAlchemy ORM lab."""

from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from .models import Base, Character, CharacterType


def create_schema(engine: Engine) -> None:
    """Create all ORM tables."""
    raise NotImplementedError


def add_character_type(session: Session, name: str) -> CharacterType:
    """Create, persist, and return a CharacterType."""
    raise NotImplementedError


def add_character(
    session: Session,
    name: str,
    health: int,
    power: int,
    character_type: CharacterType | None = None,
) -> Character:
    """Create, persist, and return a Character."""
    raise NotImplementedError


def get_character(session: Session, character_id: int) -> Character | None:
    """Return one Character by primary key, or None."""
    raise NotImplementedError


def list_characters(session: Session) -> list[Character]:
    """Return all characters ordered by id."""
    raise NotImplementedError


def strong_characters(session: Session, minimum_power: int) -> list[Character]:
    """Return characters with power >= minimum_power, highest first."""
    raise NotImplementedError


def characters_by_type(session: Session, character_type_name: str) -> list[Character]:
    """Return characters belonging to the named character type."""
    raise NotImplementedError


def update_health(session: Session, character_id: int, new_health: int) -> bool:
    """Update health; return True if found, otherwise False."""
    raise NotImplementedError


def delete_character(session: Session, character_id: int) -> bool:
    """Delete a character; return True if found, otherwise False."""
    raise NotImplementedError
