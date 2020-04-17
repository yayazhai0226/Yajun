"""
红绿灯，红灯30秒，绿灯35秒，黄灯3秒

"""

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while  True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")

"""
使用代码，实现一个注册功能。用户输入账号和密码，
要求账号5-8位
密码6-12位
账号必须是小写开头
储存到字典中，{username：password}

"""

# a = (1,2,3,"nihao","wohao","dajiahao","douhao")
# print(a[5])

# b = [1,2,3,4,"nihao","wohao"]
# print(b[4])

# c = {"username":"zhai","password":"ya"}
# print(c[1])


# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >= 5 and len(username) <= 8:
#     if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功！",{username:password})
#         else:
#             print("密码必须8-12位！")    
#     else:
#         print("账号的首字母必须是小写字母开头！")    
# else:
#     print("账号的长度不符合规范，请输入5-8位账号！") 


"""
定义一个方法，判断用户输入的账号密码是否符合规范

"""
# def checkname(username,password):
# if len(username) >= 5 and len(username) <= 8:
#     if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功！",{username:password})
#         else:
#             print("密码必须8-12位！")    
#     else:
#         print("账号的首字母必须是小写字母开头！")    
# else:
#     print("账号的长度不符合规范，请输入5-8位账号！") 

# checkname()

"""
使用代码完成一个登陆和注册的功能，并且要求，数据要存到数据库中
"""
import pymysql

def zhuce(sql):
    db = pymysql.connect(host = "47.105.178.190",user = "root",password = "123456",db = "ljtestdb")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    return True
    db.close

sql = "insert into t_user (id,username,phone,password,email) values (55,"tangwei123","13540718510","12345678","845671607@qq.com");"  
a = zhuce(sql)
print(a)




"""

使用Python  完成一个业务流程
"""




















