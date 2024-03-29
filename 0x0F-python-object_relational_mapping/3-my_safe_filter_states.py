#!/usr/bin/python3
"""  lists all match state from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur=db.cursor()
    search = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY name ASC", (f"%{search}%",))
    res = cur.fetchall()
    for re in res:
        print(re)
    cur.close()
    db.close()
