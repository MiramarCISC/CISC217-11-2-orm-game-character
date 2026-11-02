"""ORM models for the Week 11 SQLAlchemy lab."""

from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all ORM models."""


class CharacterType(Base):
    """A character classification such as Mage or Warrior."""

    __tablename__ = "character_types"

    # TODO: Add id primary key.
    # TODO: Add required name field.
    # TODO: Add one-to-many relationship to Character.


class Character(Base):
    """A game character stored in the database."""

    __tablename__ = "characters"

    # TODO: Add id primary key.
    # TODO: Add required name, health, and power fields.
    # TODO: Add optional type_id foreign key.
    # TODO: Add relationship back to CharacterType.
