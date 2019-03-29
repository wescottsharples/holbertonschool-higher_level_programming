#!/usr/bin/python3
"""
displays all states that match argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database and create cursor
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # select and list states in database
    cur.execute("
                SELECT *
                FROM states
                WHERE name='{}'
                ORDER BY id ASC".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        if (state[1] == argv[4]):
            print(state)

    # cleanup
    cur.close()
    db.close()
