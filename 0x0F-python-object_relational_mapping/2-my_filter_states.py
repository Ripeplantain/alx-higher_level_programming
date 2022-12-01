#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
Lists all states in a database
taking an arguement
"""
if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE"
        " '{:s}' ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
