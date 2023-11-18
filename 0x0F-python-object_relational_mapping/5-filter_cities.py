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
            cur.execute("""SELECT cities.name
                        FROM states
                        INNER JOIN cities
                        ON states.id = cities.state_id
                        WHERE states.name LIKE '%{}'
                        ORDER BY cities.id ASC""".format(sys.argv[4]))

            query_rows = cur.fetchall()
            if len(query_rows) > 0:
                results = f'{query_rows[0][0]}'
                for row in query_rows[1:]:
                    results = results + f', {row[0]}'

                print(results)
            break
    cur.close()
    cur2.close()
    database.close()
