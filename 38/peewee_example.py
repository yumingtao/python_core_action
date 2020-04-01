# 安装ORM框架peewee
"""
1. pip install peewee
"""
import peewee as peewee


db = peewee.MySQLDatabase("mysql", user="root", password="1234")

class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def save_price():
    Price.create_table()
    price = Price(timestamp="2020-04-01 12:20:20", BTCUSD="12345.67")
    price.save()

