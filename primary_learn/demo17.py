import pymysql
'''
红绿灯，红灯30秒，绿灯35秒，黄灯3秒

'''
# light = {'红灯':30,'绿灯':35,'黄灯':3}
# while True : # 可以实现死循环。
#     for i in light : # 默认循环的值是  key
#         for j in range(light[i]) : #想要循环的变成 value。用到light[i]
#             print(i,'倒计时还有',light[i] - j,'秒')


'''
使用代码实现用户注册功能
用户输入的账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
存储到字段中，{username:password}
'''

# username = input('请输入账号：')
# password = input('请输入密码：')
# if len(password) >= 6 and len(password) <= 12 :
#     if len(username) >=5 and len(username) <= 8 :
#         if username[0] in 'qwertyuiopasddghkjlzxcvbmn': #首字母，就是username[0]
#                     print('注册成功!',{username:password}) 
#         else :
#             print('密码需要小写开头')
#     else :
#         print('账号长度应为：5-8位')
# else :
#     print('密码需要在6-12位')


# for i in range(10) :
#     if i == 4 :
#         continue #【跳过】本次循环。往后继续
#     print(i)

# for i in range(10) :
#     if i == 4 :
#         break  #【跳出】本次循环。往后本循环结束了，只跳出一层循环
#     print(i)

'''
方法/函数的定义
'''

# def checkname(username): 
#     '''
#     说明：判断账号的规范性：账号长度是5-8位，并且账号必须小写开头
#     '''
#     if len(username) >=5 and len(username) <= 8 :
#         if username[0] in 'qwertyufiopasddghkjlzxcvbmn': #首字母，就是username[0]
#                     print('ok') 
#         else :
#                 print('账号需要小写开头')
#     else :
#         print('账号长度应为：5-8位')

# checkname('fa2333')


# def jiafa(a , b):
#     '''
#     说明：实现两个数字的相加
#     '''
#     if type(a) is int and type(a) is int :
#         print(a , '和' , b ,'的和是：',a+b)
#     else :
#         print('输入的数据类型不正确')

# jiafa(23,999)


'''
注：方法的返回值
return
'''
# a = []
# print(a.append('哈哈')) # 为什么打印的结果是：None 而不是 ['哈哈']

# def jiafa(a , b):
#     '''
#     说明：实现两个数字的相加
#     '''
#     if type(a) is int and type(a) is int :
#         return(a , '和' , b ,'的和是：',a+b) #有返回值，便于引用
#     else :
#         return('输入的数据类型不正确')

# a = jiafa(3333,55)
# print(a)


'''
异常捕获
代码报错就是异常
'''

'''
异常类:提供了报错信息。 Exception
'''
# try :
#     print(''+1)    
# except Exception as e:
#     print('上面的代码写错了' , e)

# a = input('请输入名字：')
# b = input('请输入年龄：')
# try :#代码明明写对了，但是用户如果乱输入时，我们该怎么反应
#     if int(b) > 18 :
#         print(a , '成年了')
#     else:
#         print('未成年')
# except Exception as e :
#     print('请输入正确的年龄')

'''
概念梳理：包-》模块-》类-》方法-》变量  它们既包含又包含
包：python 里面 ../lib/ 下面的文件夹就是放包的。 import 包名；比如： import time ; import random ; 除了自带，可以去下载包： pip install 包名 ; pip uninstall 包名 ； pip list ;
常用的第三方包：
pymysql selenium appium requests xlrd xlwt
模块：一个包下面可以有多个模块。  每个.py文件就是模块
'''

db = pymysql.connect(host = '59.110.143.227',user = 'root',password = '1qaz!QAZ' , dbname = 'test')
cur = db.cursor()
try :
    cur.execute('select * from table_a ;')
    res = cur.fetchall()
    print(res)
except :
    print('sql语句错误')


