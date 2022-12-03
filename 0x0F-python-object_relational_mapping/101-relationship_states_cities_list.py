#!/usr/bin/python3
"""
List all state objects using sql alchemy
with relationships
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}: {}".format(city.id, city.name))

    