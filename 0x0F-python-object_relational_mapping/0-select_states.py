#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Get MySQL username, password and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to get all states from the database
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print the state ID and name for each row
    for row in rows:
        print(row)

    # Close the database connection
    db.close()
