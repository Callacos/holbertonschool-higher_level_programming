#!/usr/bin/python3
""""
This is Elon MUSK
"""
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]


    db = None
    cursor = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states \
                       WHERE `name` = %s \
                       ORDER BY id ASC", (state,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
