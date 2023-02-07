#!/usr/bin/python3
""" State Module for HBNB project """
import models
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
            for _ids, city in models.storage.all().items():
                cls, _id = _ids.split(".")
                if cls == "City":
                    if city.state_id == self.id:
                        cities.append(city)
            return cities
