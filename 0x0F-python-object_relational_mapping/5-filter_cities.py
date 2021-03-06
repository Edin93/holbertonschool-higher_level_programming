#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def display_cities():
    arg = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=arg[1],
        passwd=arg[2],
        db=arg[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    cmd = "SELECT c.name FROM cities c LEFT JOIN states s ON c.state_id=s.id\
 WHERE s.name=%(search)s ORDER BY c.id ASC"
    cursor.execute(cmd, {'search': arg[4]})
    rows = cursor.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i != len(rows) - 1:
            print(", ", end="")
    print()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    display_cities()
