#!/usr/bin/python3
"""
Contains class definiton state class
And Base - An instance of declarative base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base =  declarative_base(metadata=mymetadata)

class State():
    """Class with id, names and attributes"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name =  Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
