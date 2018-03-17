import peewee

database = peewee.SqliteDatabase('my.db')

class Quotes(peewee.Model):
    textqoute = peewee.CharField()
    date = peewee.CharField()

    class Meta:
        database = database

if database:
    Quotes.create_table(True)
