"""
元组：里面可以装所有数据类型，也包括元组、数组、字典
下标：从0开始的；不要超出范围（越界）
a.index() 查找值做对应的下标；数据太多，用查找才合理；(就近原则)
a.count() 统计某个值的数量
"""

# a = (1,2,3,"哈哈","哈哈","嘻嘻","帅气","过分","哈哈","哈哈",True,False)
# print(a)  
# print(a[3]) 
# print(a[-3]) 
# print(len(a[4]))
# print(a.index("哈哈"))
# print(a.count("哈哈"))

"""
二维元组：
"""
# a = (1,2,3,"哈哈","哈哈","嘻嘻","帅气","过分","哈哈","哈哈",True,False)
# b = (a,"哈哈","呵呵")   #里面有3个值
# print(b[1])
# print(b[0][2])

# print(a[0:4])   # 切片：（批量取值）(左闭右开)
# print(a[4:6])
# print(a[6:])
# print(a)

"""
数组：  与元组区别：元组写好不可改，数组可改
a.append()    加数据
a.insert()    插入数据
a.index()     查找
a.count()     数
a.pop()     剪切
a.remove()  删除；后面加的是数据，不是加下标
a.clear()   清空
下标用法也和元组一样的，

"""
# a = [1,2,3,"哈哈","哈哈","嘻嘻","帅气","过分","哈哈","哈哈",True,False]

# print(a)
# a.append("再见不再见")
# a.append("相见")
# a.insert(0,"仙人")
# a.pop(4)
# print(a)
# a.remove("哈哈")
# print(a)

"""
字典： 
字典中没有顺序
结构是键值对    key:value
取值：元组、数组、字典取值都有中括号    []
新增：
修改：
"""
# a = {"name":"zhangfei","age":67,0:"yes"}
# b = a.get("name")
# c = a["name"]
# print(b+c)

# a = {"name":"yayazhai","age":16,"sex":"boy","choice":"girl"}
# print(a["name"])    #取值
# a["dream"] = "teacher"  #新增
# print(a)
# a["name"] = "yajun"     #修改
# print(a)



# a = {"name":"yayazhai","age":16,"sex":"boy","choice":"girl"}
# print(a)
# print(a["name"])
# a["dream"] = "teacher"
# print(a)
# a["name"] = "吴广"
# print(a)
"""
a.get()     取值（与a[name]区别）
a.pop()     剪切（取值）
a.update()  新增或修改

"""

# a = {"name":"yayazhai","age":16,"sex":"boy","choice":"girl"}
# b = a.get("name")
# print(a)
# print(b)
# b = a.pop("name")
# print(b)
# print(a)
# print(a.get("name"))    #为空
# print(a["name"])    #会报错


# a = {}
# a["name"] = input("name:")
# a["age"] = input("age:")
# a["sex"] = input("sex:")

# lkjjj
# print(a)


dict = {"name":"zhai","age":19}
dict1 = {"high":183}
dict1.update(dict)
print(dict1)
