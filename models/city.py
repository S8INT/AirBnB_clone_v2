#!/usr/bin/python
""" Defines class City"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Representation of class city """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")

    else:
        state_id = ""
        name = ""


    def __init__(self, *args, **kwargs):
        """ initializes class city """
        super().__init__(*args, **kwargs)
