#!/usr/bin/python3
# script that lists all states from the database
import MySQLdb
import sys

if __name__ == "__main__":
    # Establish connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # create a cursor by executing the 'cursor' function of database
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
