#!/usr/bin/python3

import MySQLdb
import sys
"""
Script that lists all states starting with cap N
"""


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("""Usage: {} needs
              <username>
              <password> and
              <database_name""".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor=db.cursor()

    query="""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN  states ON cities.state_id = states.id
            ORDER BY id ASC"""
    
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
