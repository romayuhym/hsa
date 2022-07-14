import random

from fastapi import FastAPI

import cache
from db import Books

app = FastAPI()


@app.get("/{book_id}")
def read_book(book_id):
    return cache.get_db(book_id)


author = ['Peter', 'Amy', 'Hannah', 'Michael', 'Sandy', 'Betty',
          'Richard', 'Susan', 'Vicky', 'Ben', 'William', 'Chuck', 'Viola']
title = ['Lowstreet 4', 'Apple st 652', 'Mountain 21', 'Valley 345',
         'Ocean blvd 2', 'Green Grass 1', 'Sky st 331', 'One way 98',
         'Yellow Garden 2', 'Park Lane 38', 'Central st 954', 'Main Road 989',
         'Sideway 1633']


@app.post("/")
def create_book():
    book = Books.create(
        id=random.randint(1, 2022),
        category_id=random.randint(1, 2),
        author=random.choice(author),
        title=random.choice(title),
        year=random.randint(1, 2022)
    )
    book.save()
    return "success"

