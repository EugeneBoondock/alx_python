#!/usr/bin/python3

import MySQLdb
import sys

"""
Script that lists all states starting with cap N
"""

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 5:
        print("""Usage: {} needs
              <username>
              <password> and
              <database_name""".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC"""

    cursor.execute(query, (state_name + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
