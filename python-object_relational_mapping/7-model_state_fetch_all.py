#!/usr/bin/python3
"""Start link class to table in database 
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

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
                           echo=True)
    
    query = "SELECT * FROM states"
    conn = engine.connect()
    result = conn.execute(query)
    
    for row in result:
        print(row)
    
    conn.close()
