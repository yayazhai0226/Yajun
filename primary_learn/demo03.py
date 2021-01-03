'''

'''
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# sex = input('请输入你的性别：')
# userinfo = {}
# # userinfo.update(name = name , age=age ,sex=sex)
# userinfo['name']=name
# print(userinfo)

'''
判断
if 
if else
if elif else
'''
# age = int(input('请输入你的年龄：'))
# if age > 60 :
#     print('你应该退休了')
# elif age > 30 :
#     print('你的家庭责任很重把')
# elif age > 20 :
#     print('规划自己的问题')
# else :
#     print('认真读书哈')

# a = input('请输入你的年龄：')
# if a == '' :
#     print('不能为空')
#     exit()
# if a in '0123456789':
#     a = int(a)
# else :
#     print('请输入正确的年龄！')
#     exit()
# if a > 18 :
#     print('成年了')
# else:
#     print('未成年')

# a = 'adsfsg'
# if type(a) is int :
#     print('是数字')
# elif type(a) is str :
#     print('是字符串')
# else :
#     print('其他')

'''
循环
while 循环
for 循环——遍历
'''
# a = 1
# while a < 10 :
#     print('hahafafsa法法a' , a )
#     a = a + 2
'''
练习用while：
有十个学生的成绩，需要录入到系统中
这些人是:张三、 李四、小梁、陈平安、猪猪
并且名字和成绩需要对应上
而且大于60 和小于60需要分开存放
'''
# highchengji = {}
# lowchengji = {}
# studentlist = ['张三','李四','小梁','陈平安','猪猪']
# a = 0
# while a < len(studentlist)-1 :
#     chengji = int(input('请输入'+studentlist[a]+'的成绩'))
#     if chengji >= 60 :
#         highchengji[studentlist[a]] = chengji
#     else :
#         lowchengji[studentlist[a]] = chengji
#     a = a + 1
# print(highchengji , lowchengji)


# a = '今天你吃了吗？'
# for i in a :
#     print(i)

# studentlist = ['张三','李四','小梁','陈平安','猪猪']
# for i in studentlist :
#     print(i)

# b = range(0,20,2) # 自动生成一个数列；【起始】，【结束】，【步长】步进/步长；左闭右开
# for i in b:
#     print(i)

'''
练习用for：
有十个学生的成绩，需要录入到系统中
这些人是:张三、 李四、小梁、陈平安、猪猪
并且名字和成绩需要对应上
而且大于60 和小于60需要分开存放
'''
# high = {}
# low = {}
# studentlist = ['张三','李四','小梁','陈平安','猪猪']
# for i in studentlist :
#     chengji = int(input('请输入'+i+'的成绩：'))
#     if chengji >= 60 :
#         high[i] = chengji
#     else : 
#         low[i] = chengji
# print('及格的人有：',high)
# print('不及格的人有：',low)


'''
练习:
99乘法表
'''
for i in range(1,10) :
    for j in range (1,i+1):
        print(i,'X',j,'=',i*j,end='   ') # end = ' '  的作用是不换行。
    print()# 打印一个空白字符串，来换行

'''
练习：
完成一个函数，实现功能为判断一个字符串是否是一个合法的ip地址
'''
a = input('请输入正确的ip地址：')

print(a)

