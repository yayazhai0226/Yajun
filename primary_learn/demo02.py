'''
基础2:
'''
'''
元组；
下标:从零开始编号；
元组自带的方法：index查询下标(索引)、count统计某个值的数量,他们只能操作一维元组
'''
# a = (1,2,'哈哈哈呵呵',1.5,2,3,True,False,False,True) # 里面可以装任何数据
# print(a[2])
# print(a[-2])#倒过来取值
# print(a.index(1))#索引出该值的下标是多少
# print(a.count(1))
# print(a[0:4])#切片  左闭右开
# print(a[:4])
# print(a[5:])

'''
二维元组
'''
# a = (1,2,'哈哈哈呵呵',1.5,2,3,True,False,False,True) # 里面可以装任何数据
# b = (a , '哈哈' ,'你好' )
# # print(b[1])
# print(b[0][2]) 

'''
数组
数组的方法：append extend index count pop
（元组写好后不可修改，但是数组可以）
'''
# a = [1,2,'哈哈哈呵呵',1.5,2,3,True,False,False,True]
# print(a[2])
# a.append('追加1')#往数组中‘增补’数据
# a.extend(['哈哈','呵呵']) # ‘延伸’数据
# print(a.count(1.5))
# b = a.pop(0) #切片
# print(b)
# print(a)
# print(len(a))
# b = "dfasglkgljkg"
# print(len(b))
# c = [1,2,3,"哈","洗","和"]
# c.insert(1,"大哥")#在对应位置插入数据，(单个数据插入)
# print(c)

'''
字典
1，字典的值没有顺序
2，字典的结构必须是键值对结构。 key:value
'''
a = {'name':'张三',0:'哈哈','age':12}
print(a['name']) #取值
a['high'] = '183cm' #可以用来增加数据
print(a)
a['name'] = '李四' #可以用来更新数据
print(a)

print(a.get('name1')) #取值方式1，不存在就会打印 none。
print(a['name1']) #取值方式2，不存在就会报错。
b = a.pop('name')



