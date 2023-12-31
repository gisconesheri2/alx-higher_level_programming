#!/usr/bin/python3
"""lists all state objects from the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()

    for state in states:
        print(type(state))
        print(type(state.__class__.__name__))
        print(f'{state.id}: {state.name}')
