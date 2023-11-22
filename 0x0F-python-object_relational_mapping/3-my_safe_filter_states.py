#!/usr/bin/python3
"""lists all states using the mysqldb"""
import MySQLdb as sqldb
import sys

if __name__ == "__main__":
    database = sqldb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], charset="utf8")

    cur = database.cursor()
    cur2 = database.cursor()
    cur2.execute("SELECT name FROM states")
    search_term = sys.argv[4]

    for name in cur2.fetchall():
        if search_term == name[0]:
            cur.execute("""SELECT *
                        FROM states
                        WHERE name LIKE BINARY '%{}%'
                        ORDER BY id ASC""".format(search_term))
            query_rows = cur.fetchall()

            for row in query_rows:
                print(row)
            break

    cur.close()
    database.close()
