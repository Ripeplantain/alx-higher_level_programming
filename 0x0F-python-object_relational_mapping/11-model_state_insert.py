#!/usr/bin/python3
"""
Adds state to the database
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modal_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()

    print(state1.id)
