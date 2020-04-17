"""
python 包的使用
安装：在终端输入：pip install pymysql
"""
"""
pymysql
"""

import pymysql

# db = pymysql.connect(host = "47.105.178.190",user = "root",password = "123456",db = "ljtestdb")   #链接数据库
# cursor = db.cursor()    #获取游标
# cursor.execute("show tables;")  #使用游标来执行sql语句
# res = cursor.fetchall() #获取所有结果(是一个二位元组)
# for i in res:
#     print(i)



# def chaxun(sql):
#     """
#     用来查询数据库用的！
#     """
#     db = pymysql.connect(host = "47.105.178.190",user = "root",password = "123456",db = "ljtestdb")   #链接数据库
#     cursor = db.cursor()    #获取游标
#     try:
#         cursor.execute(sql) #使用游标来执行sql语句
#         res = cursor.fetchall() #获取所有结果(是一个二位元组)
#         return res
#     except Exception as e :
#         return "sql语句错误",e

# a = chaxun("show tables;")
# print(a)


# def xiugai(sql):
"""
修改数据库里面的数据，包括新增、修改、删除
"""
#     db = pymysql.connect(host = "47.105.178.190",user = "root",password = "123456",db = "ljtestdb")



# class Db:
#     def __init__(self,host,user,password,dbname):
#         se lf.host = host
#         self.user = user
#         self.password = password
#         self.dbname = dbname

#     def chaxun(sql):
#         """
#         用来查询数据库用的！
#         """
#         db = pymysql.connect(host = self.host,user = self.user,password = self.password,db = self.dbname)   #链接数据库
#         cursor = db.cursor()    #获取游标
#         try:
#             cursor.execute(sql) #使用游标来执行sql语句
#             res = cursor.fetchall() #获取所有结果(是一个二位元组)
#             return res
#         except Exception as e :
#             return "sql语句错误",e


# def xiugai(sql):
# """
# 修改数据库里面的数据，包括新增、修改、删除
# """
# db = pymysql.connect(host = self.host,user = self.user,password = self.password,db = self.dbname)   #链接数据库
#     cursor = db.cursor()    #获取游标
#     try:
#         cursor.execute(sql) #使用游标来执行sql语句
#         res = cursor.fetchall() #获取所有结果(是一个二位元组)
#         return res
#     except Exception as e :
#         return "sql语句错误",e







