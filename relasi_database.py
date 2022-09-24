import datetime
from peewee import  *

sql_db = SqliteDatabase('bisa3.db')

class BaseModel(Model):
    class Meta:
        database = sql_db


class User(BaseModel):
    username = CharField(unique=True)

class Twet(BaseModel):
    user = ForeignKeyField(User,backref='tweet')
    pesan= TextField()

sql_db.connect()
sql_db.create_tables([User,Twet],safe=True)


data = [{'Joni','Halo ini tweet saya'},
        {'Roland','Halo Dunia'},
        {'Messi','Lagi Main Bola'}]

for username, tweets in data:
    user = User.create(username = username)
    for tweet in tweets:
        Twet.create(user = user , pesan = tweet)









