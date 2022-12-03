#!/usr/bin/python3
"""
Contains class definiton city class
And Base - An instance of declarative base
"""

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base

mymetadata = MetaData()
Base =  declarative_base(metadata=mymetadata)

class State(Base):
    """Class with id, names and attributes"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name =  Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
