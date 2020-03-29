#!/usr/bin/python3
"""
Module contains a script that lists all City objects from
the database hbtn_0e_101_usa."""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, City

def list_cities():
    """
    Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa.
    """
    Base = declarative_base()
    arg = sys.argv
    url_base = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State):
        print(s.id, ": ",  s.name, sep="")
        for c in session.query(City).filter(City.state_id == s.id):
            print("\t", c.id, ": ", c.name, sep="")
    session.close()


if __name__ == "__main__":
    list_city()
