#!/usr/bin/python3

""" Script to list all State and corresponding
City objects in the database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(connection_str.format(username, password, database))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("State {}: {}".format(state.id, state.name))
        if state.cities:
            for city in state.cities:
                print("\tCity {}: {}".format(city.id, city.name))
        else:
            print("\tNo cities found for this state")

    session.close()
