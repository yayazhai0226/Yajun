
"""
类：
用class 声明类的名字；
类的名字首字母必须大写；
默认属性方法 __init__；
使用__init__来接受参数；
每个类里面的方法，第一个参数必须是self；


面向对象编程：
类里面所有的方法，都必须要传一个参数，叫self。其他参数没要求
class Girlfriend():
    def_init_():     #写法是固定的



"""
class Girlfriend():
    """
    这是你的女朋友
    """
    def __init__(self,sex,high,weight,hair,age):    #__init__  初始化类，设定参数
        self.sex = sex  #self 来引用成员变量
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    def caiyi(self,num):
        """
        才艺表演
        """
        print("你的性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友正在：")
        if num == 1:
            print("胸口碎大石!")
        elif num == 2:
            print("唱歌")
        else:
            print("单手开瓶盖")
    def chuyi(self):
        """
        厨艺
        """
        print("精通八大菜系，啥都会做！")
    def work(self):

        """
        技能
        """
        print("开挖掘机！")


"""
类的实例化：
"""
# zhangsan = Girlfriend("女","167","56kg","大波浪","22岁")
# print(zhangsan)
# zhangsan.caiyi(1)
# zhangsan.work()



# class Car():
#     def __init__(self,pinpai,yanse,neishi):
#         self.pinpai = pinpai
#         self.yanse = yanse
#         self.neishi = neishi
#         print("你拥有了一辆"+self.pinpai+"，并且是"+self.yanse+"的，配置是"+self.neishi+"的")
#     def bianxing(self):
#         print("车子变身为喜洋洋！")
    
#     def fly(self):
#         print("车子开始起飞")

# zhangsan = Car("马自达","红色","真皮")
# zhangsan.bianxing()
# zhangsan.fly()

# class House():
#     def __init__(self,mianji,louceng,chaoxiang):
#         self.mianji = mianji
#         self.louceng = louceng
#         self.chaoxiang = chaoxiang
#     def shangquan(self):
#         print("中央商务区")

# myhouse = Car("125","16","南")
# myhouse.shangquan()


"""
继承
"""
# class Nvyou(Girlfriend):    #继承(Girlfriend:父类；Nvyou:子类；)
#     pass
# zhangsan = Nvyou("女","167","56kg","大波浪","22岁")
# zhangsan.work()

"""
重写/多态
"""

class Nvyou(Girlfriend):
    def work(self):
        print("搓澡")

zhangsan = Nvyou("女","167","56kg","大波浪","22岁")
zhangsan.work()






"""
模块的导入，以及方法的导入
# """
# import dbtools

# a = dbtools.chaxun("show tables;")
# print(a)
"""
只导入方法
"""
# from dbtools import chaxun 

"""
导入类，方法  #这样参数可以一改全改
"""
from dbtools import Db

db = Db("47.105.178.190","root","123456","ljtestdb")    #对类实例化
a = db.chaxun("show tables;")
print(a)






