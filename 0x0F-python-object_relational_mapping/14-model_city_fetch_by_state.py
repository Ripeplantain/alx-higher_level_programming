#!/usr/bin/python3
"""
Fetch by city name 
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))