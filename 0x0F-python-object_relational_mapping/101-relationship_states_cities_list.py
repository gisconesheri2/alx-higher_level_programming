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

#    city_result = session.result(#State.id, State.name, City.id, City.name#)\
    city_result = session.query(State, City)\
        .join(State.cities)\
        .order_by(State.id, City.id).all()

    prev_state_id = 0
    for result in city_result:
        current_state_id = result[0].id
        if current_state_id == prev_state_id:
            print(f'\t{result[1].id}: {result[1].name}')
        else:
            print(f'{result[0].id}: {result[0].name}')
            print(f'\t{result[1].id}: {result[1].name}')

        prev_state_id = current_state_id

    session.close()
