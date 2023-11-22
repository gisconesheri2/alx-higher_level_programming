#!/usr/bin/python3
"""lists the first state objects from the database"""

from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    current_states = session.query(State).all()
    found = False
    st = sys.argv[4]
    for s in current_states:
        if s.name.lower() == st.lower():
            found = True
            print(s.id)
    if found is False:
        print("Not found")
