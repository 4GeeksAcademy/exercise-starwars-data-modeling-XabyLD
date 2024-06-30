import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable= False)
    password = Column(String(250), nullable = False, unique = True)
    email = Column(String(250), nullable=False, unique = True)


class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer,  primary_key= True, nullable = False)
    name = Column(String(250), nullable = False)
    age = Column(Integer)
    description = Column(String(250))
    gender = Column(String(20))
    species = Column(String(20))

class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    distance = Column(Integer)
    description = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(Integer , primary_key = True, nullable = False)
    name = Column(String(50), nullable = False)
    model = Column(String(50), nullable = False)
    created = Column(DateTime , nullable = False)
    number_passengers = Column(Integer)
    capacity = Column(Integer)




class User_Favourites(Base):
    __tablename__ = 'user_favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    saved_planets = Column(String(250), ForeignKey('planets.id'), nullable = False)
    saved_characters = Column(String(250), ForeignKey ('characters.id'), nullable = False)
    saved_vehicles = Column(String(250), ForeignKey("vehicles.id"),nullable=False)
    user_favourites = relationship(User)
    from_character = relationship(Characters)
    from_planets = relationship(Planets)
    from_vehicles = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
