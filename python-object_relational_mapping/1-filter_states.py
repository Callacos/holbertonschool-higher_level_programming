#!/usr/bin/python3
""""
this
"""
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print("Usage: {} username password database".format(sys.argv[0]))
            sys.exit(1)

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states \
                    WHERE CONVERT (`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%' ORDER BY `id` ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
