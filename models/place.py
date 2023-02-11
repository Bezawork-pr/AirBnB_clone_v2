#!/usr/bin/python3
""" Place Module for HBNB project 
This file will create a table using sql alchemy"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from os import getenv

association_table = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id",ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay 
    a table created with sql alchemy
    """
    __tablename__="places"
    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'),
                    nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                    nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref="places")
    amenities = relationship('Amenity', secondary='place_amenity', back_populates="place_amenities", viewonly=False)
    #amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            "Getter"
            list_review = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    list_review.append(review)
            return list_review

        @property
        def amenities(self):
            "Getter"
            list_amenities = [] 
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    list_amenity.append(amenity)
            return list_amenities
        
        @amenities.setter
        def amenities(self, value):
            "Setter"
            if type(value) == "Amenity":
                self.amenity_ids.append(value.id)
