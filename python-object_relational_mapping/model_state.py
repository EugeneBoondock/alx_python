#!/usr/bin/python3

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
Start link class to table in database
"""

Base = declarative_base()

class State(Base):
    """
    Class uses sqlalchemy and inherits Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""Usage: {} 
              <username>
              <password>
              <database_name>
              """.format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('''mysql+mysqldb:
                           //{}:{}@localhost/{}'''
                           .format(username, 
                                   password, 
                                   database), 
                                   pool_pre_ping=True)
    Base.metadata.create_all(engine)
