"""
判断、循环、方法定义、异常捕获
if/while/for/def/try except
"""
# a = 1
# b = 2
# if a > b :
#     print("a比b大")
# else:
#     print("b更大")


# age = int(input("输入你的年龄："))
# if age > 60:
#     print("请退休")
# elif age > 40:
#     print("家庭重担")
# elif age > 20:
#     print("职业发展")
# else:
#     print("好好读书")
    
# a = "你好"
# if a in ("你好","我帅不帅？","你很帅"):
#     print("好问题")
# else:
#     print("瞎问问题")

a = input("请输入你的年龄：")
for i in a:
    if i in "0123456789":
        res = "输入的年龄为："+a
    else:
        res = "请输入正确年龄!"
print(res)

try:




# a = 1
# while a < 10 :
#     print("越小越年轻",a)
#     a = a + 1

# a = {}
# b = {}
# student = ["张","王","李","陈","余"]
# c = 0

# while c < len(student)
#     chengji = int(input("请输入"+student[c]+"的名字：")
#     if chengji >= 60:
#         high[student[c]]



#     c = c + 1
# c = len(student)

# zhangsan = int(input("张三的成绩："))
# lisi = int(input("李四的成绩："))
# if zhangsan > 60:
#     a.append("""张三":"zhangsan"")
#     print(a)
# else:
#     b.append(""张三":"lisi"") 
#     print(b)

# high = {}
# low = {}
# studentlist = ["张飞","刘备","关羽","赵云"]
# a = 0
# while a < len(studentlist):
#     chengji = int(input("请输入"+studentlist[a]+"的成绩："))
#     if chengji >= 60:
#         high[studentlist[a]] = chengji
#     else:
#         low[studentlist[a]] = chengji
#     a = a + 1
# print("及格的：",high)
# print("不及格的：",low)

# a = ["无","法","无","天","哇"]
# for i in a:
#     print(i)

# b = list(range(0,10))
# print(b)

# b = list(range(0,15,2))
# print(b)

# for i in range(0,10):
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end = " ")
#     print()


# i = 1
# while i < 10:
#     print("你好")
#     i = i + 1

# i = 3
# j = i%68
# while j < 68:
#     ptint("fsafsfs")
#     if j > 4:
#         print("秒")
#     elif j > 2:
#         print("绿灯")
#     elif j > 0:
#         pri\nt("红灯")
#     i = i + 1


# for i in range(10):
#     if i == 4:
#         continue
#     print(i)

# for i  in range(10):
#     if i ==4:
#         break
#     print(i)

    
# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == 4:
#             break
#         print(i,"X",j,"=",i*j,end = " ")
#     print()

# def jiafa(a,b):
#     if type(a) is int and type(b) is int:
#         print(a + b)
#     else:
#         print("输入正确数据类型！")

# jiafa(23,64)

# def yushu(a):
#     if type(a) is int:
#         print(a%5)
#     else:
#         print("只能输入数字") 

# yushu(7)


# a = input("输入姓名：")
# b = input("输入年龄：")
# try:
#     if int(b) > 18:
#         print(a,"成年")
#     else:
#         print(a,"未成年")
# except:
#     print("输入正确年龄！")










    