#!/usr/bin/python3
"""
Module contains a script that lists all City objects from
the database hbtn_0e_101_usa."""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base


def list_cities():
    """
    Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa.
    """
    arg = argv
    url_base = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id.asc()):
        print(s.id, ': ', s.name, sep='')
        for c in s.cities:
            print("\t", c.id, ": ", c.name, sep="")


if __name__ == "__main__":
    list_cities()
