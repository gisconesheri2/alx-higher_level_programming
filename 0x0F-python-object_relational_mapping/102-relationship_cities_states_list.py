#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa
uses the state relationship to access to the State object
linked to the City object
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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    session.close()
