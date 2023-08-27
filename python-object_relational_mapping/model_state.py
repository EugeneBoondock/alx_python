#!/usr/bin/python3

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    state_name = Column(String(250))

if len(sys.argv) != 4:
    print("Usage: {}  enter <username> <password> <database_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(f"sqlite://{username}:{password}@localhost/3306/{database}")
Base.metadata.createall(engine)