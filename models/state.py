#!/usr/bin/python3
""" Defines class State """

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Represents class state """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""


    def __init__(self, *args, **kwargs):
        """ initializes class state """
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter attribute that returns City instances """
            all_cities = models.storage.all(City)
            city_list = []
            for city in values_city:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
