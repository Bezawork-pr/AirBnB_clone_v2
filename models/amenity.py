#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
#from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column


class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities", viewonly=False)
    #id: Mapped[int] = mapped_column(primary_key=True)
