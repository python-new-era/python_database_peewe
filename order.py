import random ,datetime
from peewee import *

sql_db = SqliteDatabase('useroko.db')

class User(Model):
    username = CharField()
    point = CharField()


    class Meta:
        database = sql_db

sql_db.connect()
sql_db.create_tables([User],safe=True)
#
#
# #
# datas = [{'username': 'joni','point': 10},
#         {'username': 'lowas','point': 11},
#         {'username': 'tery','point': 34}
#         ]
# #
# User.insert_many(datas).execute()

us = User.select().order_by(User.point.asc())
for ser in us:
    print(ser.username +' - ' + ser.point)
#
