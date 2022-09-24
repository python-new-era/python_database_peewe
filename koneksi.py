from peewee import *
sql_db = SqliteDatabase('siap.db')

class User(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sql_db


sql_db.connect()
sql_db.create_tables([User],safe='true')

# User.insert(name='sinka',email='sinkaya@yahoo.com').execute()

# insert sekali banyak

# datasource = [
#     {'name':'renata','email':'renata@yahoo,com'},
#     {'name':'linda','email':'linda@yahoo,com'},
#     {'name':'daniya','email':'daniya@yahoo,com'}
# ]
#
# User.insert_many(datasource).execute()


# pisahkan field dan isi

# field = [User.name,User.email]
# data = {('gisela','gisela@yahoo.com'),
#         ('melodi','melodi@yahoo.com')
#         }
#
# User.insert_many(data,fields=field).execute()

# Tampilkan data berdarkan id

# nama = User.get(User.id == 9)
#
# print(nama.name)

#  Tampilkan data berdarkan id lebih mudah

# user = User[5]
# print(user.name)


# Menggunakan Metode Select

# query = User.select()
# for user in query:
#     print(f'{user.name} - {user.email}')

# query = User.select().where((User.name == 'sinka') | (User.name == 'melodi' ))
# for user in query:
#     print(user.name)


# mencari data

query = User.select().where(User.email.contains('@'))
for user in query:
    print(user.email)

