import random
import time
import psycopg2

# forming connection
conn = psycopg2.connect(
    database="mydb",
    user='db_usr',
    password='db_pwd',
    host='127.0.0.1',
    port='5432'
)
conn.autocommit = True

# creating a cursor
cursor = conn.cursor()

sql = "INSERT INTO books VALUES(%s,%s,%s,%s,%s)"
author = ['Peter', 'Amy', 'Hannah', 'Michael', 'Sandy', 'Betty',
          'Richard', 'Susan', 'Vicky', 'Ben', 'William', 'Chuck', 'Viola']
title = ['Lowstreet 4', 'Apple st 652', 'Mountain 21', 'Valley 345',
         'Ocean blvd 2', 'Green Grass 1', 'Sky st 331', 'One way 98',
         'Yellow Garden 2', 'Park Lane 38', 'Central st 954', 'Main Road 989',
         'Sideway 1633']


def main():
    values = []
    for id_ in range(1, 1000001):
        values.append(
            (
                id_,  # id
                random.randint(1, 2),  # category_id
                random.choice(author),  # author
                random.choice(title),  # title
                random.randint(1, 2022)  # year
            )
        )
        if id_ % 1000 == 0:
            cursor.executemany(sql, values)
            conn.commit()
            values = []


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

conn.close()
