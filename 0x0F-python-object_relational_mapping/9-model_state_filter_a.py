#!/usr/bin/python3
"""
List all state objects using sql alchemy
Contains the letter 'a
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modal_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%')).all()

    for state in states:
        print("{} {}".format(state.id,state.name))