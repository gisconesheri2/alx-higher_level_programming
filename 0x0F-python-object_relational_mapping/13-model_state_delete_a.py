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

    state = session.query(State)\
        .filter(State.name.ilike('%a%'))\
        .delete(synchronize_session='fetch')
    session.commit()
    session.close()
