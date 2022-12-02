#!/usr/bin/python3
"""
Takes in arguement input
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modal_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == sys.argv[4]).first()

    for state in states:
        print("Not found" if not state else state.id)