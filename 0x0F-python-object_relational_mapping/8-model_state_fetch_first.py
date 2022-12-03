#!/usr/bin/python3
"""
List all state objects using sql alchemy
ordered by State.id
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).orderby(State.id).first()

    for state in states:
        print("Nothing" if not state else "{} {}".format(state.id,state.name))
        