#!/usr/bin/python3
"""model from the table cities"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import State, Base


class City(Base):
    """table model schema for a city class"""

    __tablename__ = "cities"

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
#    state = relationship("State", backref="cities")

    def __init__(self, name):
        """initialize the city name"""
        self.name = name
