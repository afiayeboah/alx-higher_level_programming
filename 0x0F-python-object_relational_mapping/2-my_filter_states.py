#!/usr/bin/python3
"""
Script that connects to a MySQL database and displays all values
in the states table where name matches the argument
provided as a command-line argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
              .format(sys.argv[4]))

    rows = c.fetchall()

    for row in rows:
        print(row)
