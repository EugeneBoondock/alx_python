#!/usr/bin/python3
"""
Lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get user input from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database)

    # Prepare the SQL query using format and user input
    query = """
            SELECT * FROM states
            WHERE name LIKE BINARY '{}%'
            ORDER BY id ASC
            """.format(state_name)

    # Create a cursor to execute the query
    cursor = db.cursor()
    cursor.execute(query)

    # Fetch and print the matching rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
