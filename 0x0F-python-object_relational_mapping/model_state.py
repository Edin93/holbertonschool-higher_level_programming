#!/usr/bin/python3
"""
This module contains the class definition of a State and an
instance Base = declarative_base()
"""


from sqlalchemy import (
    inspect,
    Column,
    String,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """The state declaration"""
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
