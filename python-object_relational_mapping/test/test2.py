#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Corrected connection string
engine = create_engine('postgresql://eugeneboondock:Philos1998@localhost:5432/eugene', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

Base.metadata.create_all(engine)
