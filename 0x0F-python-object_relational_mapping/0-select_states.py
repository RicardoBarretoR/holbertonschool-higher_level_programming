#!/usr/bin/python3
# script that lists all states from the database
import MySQLdb

if __name__ == "__main__":
    # Establish connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")
    # create a cursor by executing the 'cursor' function of database
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
