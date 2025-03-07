#!/usr/bin/python3
""""
This is Elon MUSK
"""
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        if len(sys.argv) != 5:
            print("Usage: {} username password database state_name".format(
                sys.argv[0]))
            sys.exit(1)

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db.cursor()
        query = "SELECT * FROM states\
            WHERE name = '{}'\
            ORDER BY id ASC".format(sys.argv[4])
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
