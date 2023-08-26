#!/usr/bin/python3

import MySQLdb
import sys
"""
Script lists all the states in a table
"""


def main():
    """
    Function takes all parameters required
    """
    if len(sys.argv) != 4:
        usage = (
            "Usage: {} <mysql_username> <mysql_password>"
            " <database_name>".format(sys.argv[0])
        )
        print(usage)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        port=3306,
        db=database
    )

    cursor = db.cursor()

    select_query = "SELECT * WHERE UPPER(user) = username FROM states ORDER BY id ASC"
    cursor.execute(select_query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
