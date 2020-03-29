#!/usr/bin/python3
"""
Module contains a script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import State
from model_city import City


def list_states():
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


if __name__ == "__main__":
    list_states()
