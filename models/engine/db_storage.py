#!/usr/bin/python3
""" This module defines a new engine 'DBStorage' """
from sqlalchemy import create_engine, MetaData
import os

HBNB_MYSQL_USER = os.environ["HBNB_MYSQL_USER"]
HBNB_MYSQL_PWD = os.environ["HBNB_MYSQL_PWD"]
HBNB_MYSQL_DB = os.environ["HBNB_MYSQL_DB"]
def DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None
    __init__(self):
        """ Initialization """
        self.__engine = create_engine("mysql+mysqldb://HBNB_MYSQL_USER:\
                                       HBNB_MYSQL_PWD@localhost/HBNB_MYSQL_DB", pool_pre_ping=True)
        if os.environ["HBNB_ENV"] == "test":
            metadata = MetaData()
            metadata.reflect(bind=engine)
            metadata.drop_all(engine)
