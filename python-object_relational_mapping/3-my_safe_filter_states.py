#!/usr/bin/python3

import MySQLdb
import sys
"""
Script that connects via MySQLdb
avoids SQL injection
"""


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""Usage: Enter username:{}
            password:{}
            db_name:{}
            state_name:{}
            """.format(sys.argv[1], 
                        sys.argv[2], 
                        sys.argv[3], 
                        sys.argv[4]))
        
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

    db = MySQLdb.connect(
        host = "localhost",
        user = "username",
        passwd = "password",
        database = "database"
    )

    query = """SELECT * FROM states
            WHERE name LIKE BINARY %s
            ORDER BY state_id ASC"""

    cursor= db.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
