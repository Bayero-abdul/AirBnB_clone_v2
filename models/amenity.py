#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Representation of an Amenity'''
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
    else:
        name = ""
