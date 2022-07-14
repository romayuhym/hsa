from peewee import PostgresqlDatabase, Model, IntegerField, CharField

db = PostgresqlDatabase(
    "mydb",
    user="db_usr",
    password="db_pwd",
    host="127.0.0.1",
    port=5432
)


class Books(Model):
    id = IntegerField()
    category_id = IntegerField()
    author = CharField()
    title = CharField()
    year = IntegerField()

    class Meta:
        database = db


