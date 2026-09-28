# Define models for a restaurant application using SQLAlchemy
# Start with imports
import os
import sys
from sqlalchemy import Column, Integer, String, Date,Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Create an instance of the declarative base
Base = declarative_base()

# Create a class for the restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    phone_number = Column(String(20))
    email = Column(String(250))
