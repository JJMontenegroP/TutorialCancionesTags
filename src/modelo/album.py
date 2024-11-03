import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(500))
    descripcion = Column(String(2000))
    ano = Column(Integer, default=0)
    medio = Column(Enum(Medio, native_enum=False))
    canciones = relationship('Cancion', secondary='album_cancion')
