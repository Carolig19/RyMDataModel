import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    planeta = Column(String(250), nullable=False)
    ubicacion = Column(String(250), nullable=False)
    estado_id = Column(String(250), ForeignKey('especie.estado'))


class Especies(Base):
    __tablename__ = 'especie'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_id = Column(String(250), ForeignKey('personaje.nombre'))
    nombre = relationship(Personajes)
    planeta = Column(String(250), ForeignKey('personaje.planeta'))
    ubicacion = Column(String(250), ForeignKey('personaje.ubicacion'))
    tipo = Column(String(250), nullable=True)
    genero = Column(String(250), ForeignKey('personaje.genero'))
    estado = Column(String(250), nullable=False)
    
class Favoritos(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), ForeignKey('personaje.nombre'))
    capitulo = Column(String(250), nullable=True)
    ubicacion = Column(String(250), ForeignKey('personaje.ubicacion'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')