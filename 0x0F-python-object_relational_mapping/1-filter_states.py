#!/usr/bin/python3
"""lists all states using the mysqldb"""
import MySQLdb as sqldb
import sys

if __name__ == "__main__":
    database = sqldb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], charset="utf8")

    cur = database.cursor()

    cur.execute("""SELECT * FROM states
                WHERE name LIKE 'N%' ORDER BY id ASC""")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    database.close()
