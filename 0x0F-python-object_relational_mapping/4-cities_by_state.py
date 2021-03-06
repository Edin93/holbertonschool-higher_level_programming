#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def list_cities():
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
    cmd = "SELECT c.id, c.name, s.name FROM cities c LEFT JOIN states s ON\
 c.state_id=s.id ORDER BY c.id ASC"
    cursor.execute(cmd)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_cities()
