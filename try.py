import sqlite3

sqliteConnection = sqlite3.connect('db.sqlite3')
cursor = sqliteConnection.cursor()

print('DB Init')
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM auth_user;")
# for i in cursor.fetchall():
#     print(i)
# print(cursor.fetchall())

# print('\n\n')
cursor.execute("SELECT sql FROM sqlite_master WHERE name='auth_user';")
for i in cursor.fetchall():
    print()
    print(i)

cursor.close()
sqliteConnection.close()

