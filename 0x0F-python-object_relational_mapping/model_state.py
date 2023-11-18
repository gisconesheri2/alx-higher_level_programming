#!/usr/bin/python3
"""Declare Base class and extend it to create
the nodel table"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """template for the states table"""
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """initiliaze the state properties"""
        self.name = name
