import random

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=4406,
    user="mydb_user",
    password="mydb_pwd",
    database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)"
name = ['Peter', 'Amy', 'Hannah', 'Michael', 'Sandy', 'Betty',
        'Richard', 'Susan', 'Vicky', 'Ben', 'William', 'Chuck', 'Viola']
address = ['Lowstreet 4', 'Apple st 652', 'Mountain 21', 'Valley 345',
           'Ocean blvd 2', 'Green Grass 1', 'Sky st 331', 'One way 98',
           'Yellow Garden 2', 'Park Lane 38', 'Central st 954', 'Main Road 989',
           'Sideway 1633']


def main():
    for _ in range(1000):
        val = (
            random.choice(name),
            random.choice(address),
            random.randint(0, 100)
        )
        mycursor.execute(sql, val)
        mydb.commit()


if __name__ == "__main__":
    main()
