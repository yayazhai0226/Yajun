"""
python 包的使用
安装：在终端输入：pip install pymysql
"""
import pymysql

# def chaxun(sql) :
#     '''
#     这个方法是查询数据库用的
#     '''
#     db = pymysql.connect(host = '59.110.143.227' , user = 'root' , password = '1qaz!QAZ' , db = 'test')
#     cursor = db.cursor() # 获取游标
#     try: #想到sql语句可能错误，加一个异常捕获
#         cursor.execute(sql) #执行语句
#         res = cursor.fetchall() # 返回结果
#         return res
#     except Exception as e :
#         return 'sql语句错误', e

# def xiugai(sql) :
#     '''
#     修改数据库的语句，包括新增，修改，删除
#     '''
#     db = pymysql.connect(host = '59.110.143.227' , user = 'root' , password = '1qaz!QAZ' , db = 'test')
#     cursor = db.cursor() #获取游标
#     try : #想到sql语句可能错误，加一个异常捕获
#         cursor.execute(sql) #执行语句
#         db.commit() #点击确定
#         return True
#     except Exception as e :
#         return 'sql语句错误'


'''
我想把上面的几个方法弄到一个 ‘类’ 里
'''
class Db:
    '''
    这是一个操作数据库的类
    '''
    def _init_(self ,host ,user ,password ,dbname,port = '3306') :
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.port = port

    def chaxun(sql) :
        '''
        这个方法是查询数据库用的
        '''
        db = pymysql.connect(host = self.host , user = self.user , password = self.password , db = self.dbname)
        cursor = db.cursor() # 获取游标
        try: #想到sql语句可能错误，加一个异常捕获
            cursor.execute(sql) #执行语句
            res = cursor.fetchall() # 返回结果
            return res
        except Exception as e :
            return 'sql语句错误', e

    def xiugai(sql) :
        '''
        修改数据库的语句，包括新增，修改，删除
        '''
        db = pymysql.connect(host = self.host , user = self.user , password = self.password , db = self.dbname)
        cursor = db.cursor() #获取游标
        try : #想到sql语句可能错误，加一个异常捕获
            cursor.execute(sql) #执行语句
            db.commit() #点击确定
            return True
        except Exception as e :
            return 'sql语句错误'
# sql = 'insert into table_a values (6,"python里面添加的") ;'
# a = xiugai(sql)
# print(a)
# b = chaxun('select * from table_a ;')
# print(b)


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







