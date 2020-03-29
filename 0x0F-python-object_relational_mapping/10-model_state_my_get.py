#!/usr/bin/python3
"""
Module contains a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa.
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def first_state():
    """
    Prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa.
    """

    arg = sys.argv
    url_base = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == arg[4]).first()
    if result is not None:
        print(result.id)
    else:
        print("Not found")


if __name__ == "__main__":
    first_state()
