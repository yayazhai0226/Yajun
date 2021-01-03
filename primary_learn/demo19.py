import pymysql

db = pymysql.connect(host = '59.110.143.227' , user = 'root' , password = '1qaz!QAZ' , db = 'test')
cursor = db.cursor()
cursor.execute('select * from table_a')
res = cursor.fetchall()
for i in res :
    print(i)




