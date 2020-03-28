#!/usr/bin/python3
import MySQLdb
"""
Lists all states from the database hbtn_0e_0_usa
"""


connection = MYSQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa",
    charset="utf8"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM STATE ORDER BY id ASC")
query_rows = cursor.fetall()
for row in query_rows:
    print(row)
cursor.close()
connection.close()
