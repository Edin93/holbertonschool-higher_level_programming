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
from relationship_city import (
    Base,
    City
)
from sqlalchemy.orm import relationship


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
    cities = relationship(
        "City",
        cascade="all,delete",
        backref="state",
    )
