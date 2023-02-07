#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.amenity import Amenity
#from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column

association_table = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id",ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__="places"
    #id: Mapped[int] = mapped_column(primary_key=True)
    #children: Mapped[List[Amenity]] = relationship(secondary=association_table)
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
    amenities = relationship('Amenity', secondary='place_amenity', back_populates="places", viewonly=False)

