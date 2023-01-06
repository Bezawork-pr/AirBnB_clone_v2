#!/usr/bin/python3                                                           
"""This module defines a class to manage the db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os
from models.place import Place
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.base_model import Base
class DBStorage:                                                           
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None
    classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                        format(os.environ['HBNB_MYSQL_USER'],
                        os.environ['HBNB_MYSQL_PWD'],
                        os.environ['HBNB_MYSQL_HOST'],
                        os.environ['HBNB_MYSQL_DB'],
                        pool_pre_ping=True))
        __session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(__session)
        self.__session = Session()
        try:
            if os.environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)
        except Exception as error:
            pass

    def all(self, cls=None):
        objects_dict = {}
        if cls is None:
            for i in DBStorage.classes:
                for j in self.__session.query(i).all(): 
                    object_dict[i+"."+j.id] = j
        else:
            for k in self.__session.query(eval(cls)).all(): 
                objects_dict[cls+"."+k.id] = k
        return objects_dict

    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        try:
           self.__session.delete(obj)
        except Exception as error:
            pass

    def reload(self):
        Base.metadata.create_all(self.__engine)
        #self.__session.expire_on_commit=False
