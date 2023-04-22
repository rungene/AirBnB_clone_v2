#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine


class DBStorage:
    """This class manages db storage of hbnb models
    _engine:(private)
    __session:(private)
    """
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        self.__engine = create_engine('mysql+mysqldb')
