#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    table_name = "states"
    column_name = "name"
    query = f"DELETE t1 FROM {table_name} t1 INNER JOIN {table_name} t2 WHERE t1.id > t2.id AND t1.{column_name} = t2.{column_name}"
    cursor.execute(query)
    db.commit()
    print(f"{cursor.rowcount} rows deleted.")
    cursor.close()
    db.close()
