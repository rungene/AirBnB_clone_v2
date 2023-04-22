#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """This class manages db storage of hbnb models
    _engine:(private)
    __session:(private)
    """
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_pass = os.environ.get('HBNB_MYSQL_PWD')
        mysql_host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        mysql_db = os.environ.get('HBNB_MYSQL_DB')
        
        if not all([mysql_user, mysql_pass, mysql_host, mysql_db]):
            raise ValueError('Please input all credentials')
        
        url_db = f'mysql+mysqldb://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}'

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        
        self.__engine = create_engine(url_db, pool_pre_ping=True)
            Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def all(self, cls=None):
        """
        Queries the current database session for all objects of a
        specified class or for all objects if cls is None
        Args:
            The class to filter objects by.if cls==None, return all objects
        Return:
            Returns a dictionary. The format
            key = <class-name>.<object-id>
            value = object
        """
        my_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                my_dict[f'{cls.__name__}.{obj.id}'] = obj
        else:
            for cls in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(cls):
                    my_dict[f'{cls.__name__}.{obj.id}'] = obj
        return my_dict                    
    
    def close(self):
        """ removes the current session from the session registry."""
        self.__session.remove()

    def get_session(self):
        """getter method for current session instance"""
        return self.__session
