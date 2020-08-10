#!/usr/bin/python3
# lists all states with a name starting with N
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
