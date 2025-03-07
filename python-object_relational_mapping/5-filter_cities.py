#!/usr/bin/python3
"""
This
"""
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        # Check if all arguments are provided
        if len(sys.argv) != 4:
            print("Usage: {} username password database state".format(sys.argv[0]))
            sys.exit(1)

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db.cursor()
        cursor.execute("""SELECT cities.name \
                    FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    WHERE CONVERT (states.name USING Latin1) \
                    COLLATE Latin1_General_CS = %s \
        			ORDER BY c.id ASC""")
        rows = cursor.fetchall()
        print(", ".join([row[0] for row in rows]))

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
