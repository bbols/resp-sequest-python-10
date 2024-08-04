import sqlite3
import pprint
con = sqlite3.connect('test.db')

#курсор

cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE data(id INTEGER PRIMARY KEY,name VARCHAR(32), region VARCHAR(64),key_skill TEXT);")
    #если запрос ничего не возвращает
except:
    pass
cursor.execute("INSERT INTO data(name,region,key_skill) VALUES('python devloper','Moscow','python');")
cursor.execute("INSERT INTO data(name,region,key_skill) VALUES('java devloper','Piter','js, sql');")

cursor.execute("SELECT * from data")
result = cursor.fetchall()
pprint.pprint(result)
print()
cursor.execute("SELECT * from data where region=?",('Moscow',))
result = cursor.fetchall()
pprint.pprint(result)