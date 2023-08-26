#!/usr/bin/python3
"""
Lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        name=sys.argv[4])
    
    data = {'name': name}

    cursor = db.cursor()
    cursor.execute("""
                   SELECT * FROM states
                   WHERE {} LIKE BINARY 'N%'
                   ORDER BY id ASC
                   """.format(data={'name': name}))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
