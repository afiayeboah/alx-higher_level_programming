#!/usr/bin/python3
"""Module for defining the State class and its relationship with the City class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_city import Base, City

Base = declarative_base()


class State(Base):
    """Represents a state in the database.

    Each State object corresponds to a row in the 'states' table.
    This class defines the structure of the 'states' table and
    its relationship with the 'cities' table.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        cities (relationship): Relationship with the City class.
            This relationship allows accessing the City objects
            associated with the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
