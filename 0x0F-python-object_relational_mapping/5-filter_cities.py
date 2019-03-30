#!/usr/bin/python3
"""
lists all cities from database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database and create cursor
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # select and list states in database
    cur.execute("""
                SELECT cities.name
                FROM cities
                INNER JOIN states ON states.id = cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC
                """, (argv[4],))
    states = cur.fetchall()
    print(", ".join(["{}".format(state[0]) for state in states]))

    # cleanup
    cur.close()
    db.close()
