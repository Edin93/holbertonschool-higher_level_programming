#!/usr/bin/python3
"""
Module contains a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import State, Base, City


def create_data():
    """
    Creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
    """
    arg = sys.argv
    url_base = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    parent = State(name='California')
    child = City(name='San Francisco')
    parent.cities.append(child)
    session.add(parent)
    session.commit()


if __name__ == "__main__":
    create_data()
