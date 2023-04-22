#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Stringi, Integer
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__:the table name, states
        name: column containing a string (128 characters)
        can’t be null
        cities:a relationship with the class City
    """
    id = Column(Integer, primary_key=True)
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """
        getter attribute
        Return:
            list of City instances with state_id equals
            to the current State.id
        """
        from models import storage
        my_list = []
        my_cities = storage.all(City).values
        for city in my_cities:
            if self.id == city.state_id:
                my_list.append(city)
        return my_list
