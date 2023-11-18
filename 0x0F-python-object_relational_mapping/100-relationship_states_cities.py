#!/usr/bin/python3
"""lists the first state objects from the database"""

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
    calif_state = State('California')
    calif_city = City('San Francisco')
    calif_state.cities.append(calif_city)

    session.add(calif_state)

    session.commit()
    session.close()
