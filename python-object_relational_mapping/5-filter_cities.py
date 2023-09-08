#!/usr/bin/python3

"""
 takes in the name of a state as an argument and lists all cities of that
 state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """connect to sql server"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    """create a cursor object"""
    cursor = db.cursor()

    """query"""
    sql = """SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id=cities.state_id
        WHERE states.name = %s
        ORDER by cities.id ASC"""

    """execute the query"""
    cursor.execute(sql, (sys.argv[4], ))

    """fetch data"""
    data = cursor.fetchall()

    """print data"""
    print(", ".join([city[0] for city in data]))

    """close cursor and connection"""
    cursor.close()
    db.close()