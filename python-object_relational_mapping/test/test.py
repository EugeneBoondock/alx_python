#!/usr/bin/python3

from MySQLdb import _mysql

db = _mysql.connect(host='localhost', user='eugeneboondock', password='Philos@1998', database='eugene')

db.query("CREATE TABLE IF NOT EXISTS poetry (id INT PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")

poems = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for poem in poems:
    db.query("INSERT INTO poetry (title) VALUES ('%s')" % poem)
    print("Auto Increment ID: %s" % db.insert_id())
    db.query("SELECT * FROM poetry WHERE id = {}" (2))
