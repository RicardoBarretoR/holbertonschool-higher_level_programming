#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Establish connection to the database"""
    user = sys.argv[1]
    password = sys.argv[2]
    basedata = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=basedata)
    """create a cursor by executing the 'cursor' function of database"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY %s \
                ORDER BY states.id ASC", (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
