#!/usr/bin/python3
"""
Module contains a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def add_state():
    """
    Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
    """

    arg = sys.argv
    url_base = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    add_state()
