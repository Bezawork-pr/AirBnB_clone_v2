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
        """Connect with Database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                        format(os.environ['HBNB_MYSQL_USER'],
                        os.environ['HBNB_MYSQL_PWD'],
                        os.environ['HBNB_MYSQL_HOST'],
                        os.environ['HBNB_MYSQL_DB'],
                        pool_pre_ping=True))
        try:
            if os.environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)
        except Exception as error:
            pass

    def all(self, cls=None):
        """Return all objects"""
        objects_dict = {}
        if cls is None:
            for i in DBStorage.classes:
                for j in self.__session.query(i).all(): 
                    object_dict[i+"."+j.id] = j
        else:
            if type(cls) is str:
                tocls = eval(cls)
            else:
                tocls = cls
            for k in self.__session.query(tocls).all():
            #for k in self.__session.query(cls).all():
                objects_dict[str(cls)+"."+k.id] = k
        return objects_dict

    def new(self, obj):
        """New obj added to session"""
        self.__session.add(obj)
    
    def save(self):
        """session commited"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from session"""
        try:
           self.__session.delete(obj)
        except Exception as error:
            pass

    def reload(self):
        """Reload from Database"""
        Base.metadata.create_all(self.__engine)
        __session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(__session)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
