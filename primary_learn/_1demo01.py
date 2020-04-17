# a = (1,2,3,"哈","囍","呵")
# print(a.count("哈"))

# b = "dfasglkgljkg"
# print(len(a))

# c = [1,2,3,"哈","洗","和"]
# c.append("你好")
# print(c)
# c.insert(1,"大哥")
# print(c)

"""
pop
"""

# c = [1,2,3,"哈","洗","和"]
# c.pop(3)
# print(c)
# d = c.pop(3)
"""
extend
"""
# c = [1,2,3,"哈","洗","和"]
# x = ["你好","可好"]
# c.extend(x)
# print(c+x)

a = [1,3,"哈"]
print(a)
b = (a,4,6)
print(b)

"""
数据类型：str int float bool tuple list dict

"""
# print("你好丑，我好帅")     #字符串   str
# print(2333)               #整数
# print(1.666)          #小数
# print(True)           #布尔值 true/fales
# print(())         #元组
# print([])         #数组
# print({})         #字典


# print("哈哈",2333,2.33)
# print("哈哈"+"嘻嘻")
# print("哈哈"*20)
# print((1+2)*100)
# print(2>3)

"""
input() 获取的内容都是  字符串

"""
# a = input("请输入数字1：")
# b = input("请输入数字2：")
# print("input获取的内容：",a+b)

# a = int(input("请输入数字1："))
# b = int(input("请输入数字2："))
# print("input获取的内容：",a+b)

"""
type() 解析数据的格式

"""
# print(type("哈哈"))
# print(type(5666))
# print(type(1.5))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

"""
任何数据都可以转换为字符串；
整数和小数可以互相转换；
字符串转换为其他类型数据，必须满足长得像！

"""
# print(type(2333))
# a = str(2333)
# print(type(a))

"""
len() 获取数据长度：只支持字符串、元组、数组、字典

"""
# a = len(input("第一段内容："))
# b = len(input("第二段内容："))
# print("两段内容长度起来有多长："，a+b)


"""
格式化字符串
"""
# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# sql = "insert into t_user (username,password) values ('{}','{}');".format(username,password)    #按顺序输入
# print(sql)


























