#!/usr/bin/python3
"""lists all states with a name starting with N """
import sys
import MySQLdb

if __name__ == "__main__":
    """Establish connection to the database"""
    user = sys.argv[1]
    password = sys.argv[2]
    basedata = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=basedata)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
