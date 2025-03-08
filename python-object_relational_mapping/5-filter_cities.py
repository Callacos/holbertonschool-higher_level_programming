#!/usr/bin/python3
"""
This
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        msg = "Usage: {} <username> <password> <database> <state>"
        print(msg.format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        cursor = db.cursor()

        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        print(", ".join(city[0] for city in cities))

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if db:
            db.close()
