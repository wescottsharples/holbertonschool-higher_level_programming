#!/usr/bin/python3
import MySQLdb
from sys import argv

db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)

cur.close()
db.close()
