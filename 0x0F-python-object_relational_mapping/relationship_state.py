#!/usr/bin/python3
"""Declare Base class and extend it to create
the nodel table"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """template for the states table"""
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    def __init__(self, name):
        """initiliaze the state properties"""
        self.name = name
