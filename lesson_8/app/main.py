import random
from datetime import date

import mysql.connector
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def create_book():
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="admin",
        password="admin",
        database="mydb"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (date_of_birth) VALUES (%s)"
    mycursor.execute(sql, (date.fromtimestamp(random.randint(0, 1658991804)).strftime('%Y-%m-%d'),))
    mydb.commit()
    return "success"

