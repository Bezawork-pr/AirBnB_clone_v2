#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

#City.states = relationship("State", order_by = State.id, back_populates = "city")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """return the list of City"""
            cities = []
            for ids, value in models.storage.all().items():
                cls, ids = ids.split(".")
                if cls.__name__ == "City":
                    cities.append(value)
            return cities
