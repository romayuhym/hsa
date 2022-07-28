import random
from datetime import date

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="admin",
    password="admin",
    database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (date_of_birth) VALUES (%s)"


def main():
    date_insert = []
    for i in range(40000001):
        date_insert.append((date.fromtimestamp(random.randint(0, 1658991804)).strftime('%Y-%m-%d'),))

        if i and i % 1000 == 0:
            mycursor.executemany(sql, date_insert)
            mydb.commit()
            date_insert = []


if __name__ == "__main__":
    main()
