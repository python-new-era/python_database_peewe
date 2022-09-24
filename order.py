import random ,datetime
from peewee import *

sql_db = SqliteDatabase('user2.db')

class User(Model):
    username = CharField()
    point = CharField()
    waktu = DateTimeField(default=datetime.datetime.now())


    class Meta:
        database = sql_db

sql_db.connect()
sql_db.create_tables([User],safe=True)

def getRand():
    return random.randint(1,2000)
#
#
# #
# datas = [{'username': 'joni','point': getRand()},
#         {'username': 'lowas','point': getRand()},
#         {'username': 'tery','point': getRand()}
#         ]
# #
# User.insert_many(datas).execute()
#
us = User.select().order_by(User.point.desc())
for ser in us:
    print(f'Namanya {ser.username} Pointnya {ser.point} waktunya {ser.waktu}')
#
