#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
uses the cities relationship to get related City objects
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')
        cities = state.cities
        for city in cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
