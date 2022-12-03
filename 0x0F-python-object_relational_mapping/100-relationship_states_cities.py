#!/usr/bin/python3
"""
Insert State with City
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

    newState = State('name=California')
    newCity = City('name=San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
