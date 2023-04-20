#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__:the table name, states
        name: column containing a string (128 characters)
        can’t be null
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
