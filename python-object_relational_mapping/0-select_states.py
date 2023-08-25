#!/usr/bin/python3

import MySQLdb
"""
SQL for Python scripts that does things
"""


def main():
    """
    Script connects to database through MySQL connect
    fetches and does other stuff
    """
    db = MySQL.connect(host='localhost', username='eugene', password='pass', port=3306, database='hbtn_0e_0_usa')

    cursor = db.cursor()

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS states
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL
    """
    select_query = ("SELECT * from states ORDER by id DESC")

    cursor.execute(select_query)

    results = cursor.fetchall()

    for row in results:
        print(row[0], row[1])

    db.close()
    cursor.close()

if __name__ == '__main__':
    main()
