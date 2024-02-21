#!/usr/bin/python3
"""Module for defining the City class and its relationship with the State class."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city in the database.

    Each City object corresponds to a row in the 'cities' table.
    This class defines the structure of the 'cities' table and
    its relationship with the 'states' table.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state to which
            the city belongs.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
