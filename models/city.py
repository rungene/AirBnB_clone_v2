#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Args
        Basemodel - super class
        Base - declarative_base()
    Attributes
        __tablename__:table name, cities
        name: column containing a string (128 characters)
        can’t be null
        state_id: column containing a string
        (60 characters)
        can’t be null
        is a foreign key to states.id
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey='states.id')
    name = Column(String(128), nullable=False)
