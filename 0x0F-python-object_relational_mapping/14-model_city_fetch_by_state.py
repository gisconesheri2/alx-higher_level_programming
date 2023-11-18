#!/usr/bin/python3
"""prints all city objects and substitutes the
the state_id state name
"""

from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(State.name, City.id, City.name)\
        .join(State)\
        .order_by(City.id).all()

    for city in all_cities:
        print(f'{city[0]}: ({city[1]}) {city[2]}')
