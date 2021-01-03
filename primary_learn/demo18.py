'''
练习：
定义一个方法，判断账号和密码是否符合规范
'''
# def checkname(username , password):
#     if len(username) >= 5 and len(username) <= 8 :
#         if username[0] in 'qwertyuiopasdfghjklzxcvbnm' :
#             if len(password) >= 8 and len(password) <= 16 :
#                 return True
#             else :
#                 return '密码不符合规范'
#         else :
#             return '账号的首字母必须小写'
#     else :
#         return '账号的长度应在5-8位'


# res = checkname('zhangsan','13323456')
# print(res)

'''
类：
class声明类；
类的名字（首字母必须大写）；
默认属性方法： __init__；（如果没有默认参数，也可以不定义默认参数）
使用__init__来接受参数；
类里面所有的方法第一个参数必须是self，其他的正常加；
'''

# class GirlFriend(): #格式是固定的！
#     '''
#     女朋友
#     '''
#     def _init_(self):   #也是固定的！
#         self.sex = '女'
#         self.high = '170cm'
#         self.weight = '55kg'
#         self.hair  = '大波浪'
#         self.age = '18岁'
#     def caiyi(self,num): #第一个参数必须是self，其他参数正常加
#         '''
#         才艺
#         '''
#         if num == 1 :
#             print('胸口碎大石!')
#         elif num == 2 :
#             print('唱跳!')
#         else :
#             print('单手开瓶盖!')
#     def chuyi(self) :
#         '''
#         厨艺
#         '''
#         print('精通八大菜系!')
#     def work(self):
#         '''
#         工作
#         '''
#         print('开挖掘机!')


'''
类的实例化
'''
# zhangsan = GirlFriend() # 类的实例化
# zhangsan.caiyi(2)
# zhangsan.work()

# print(zhangsan.sex)

'''
当然，类也可以传参数的.注意要在 _init_ 后面传
'''
# class GirlFriend(): #格式是固定的！
#     '''
#     女/男朋友
#     '''
#     def __init__(self,sex,high,weight,hair,age):   #也是固定的！
#         self.sex = sex
#         self.high = high
#         self.weight = weight
#         self.hair  = hair
#         self.age = age
#     def caiyi(self,num): #第一个参数必须是self，其他参数正常加
#         '''
#         才艺
#         '''
#         if num == 1 :
#             print('胸口碎大石!')
#         elif num == 2 :
#             print('唱跳!')
#         else :
#             print('单手开瓶盖!')
#     def chuyi(self) :
#         '''
#         厨艺
#         '''
#         print('精通八大菜系!')
#     def work(self):
#         '''
#         工作
#         '''
#         print('开挖掘机!')

# zhangsan = GirlFriend('男','183cm','90kg','锡纸烫','32岁')
# zhangsan.caiyi(1)


# class Car():    #其实  object 是祖宗类（原始类）。  class Car(object):
#     def __init__(self , pingpai , yanse , neishi , jilun) :
#         self.pingpai = pingpai
#         self.yanse = yanse
#         self.neishi = neishi
#         self.jilun = jilun
    
#     def bianxing(self) :
#         print('车子变形喜洋洋')
    
#     def fly(self) :
#         print('车子开始起飞')
    
# zhangsan = Car('奥拓','五颜六色','豪华内饰','独轮')
# zhangsan.fly()

'''
类的继承：
'''
# class NvPengYou(GirlFriend):    #在括号里面输入被继承的类。于是它就获得了继承的方法等等. 一个是父类；一个是子类；其实  object 是祖宗类（原始类）。
#         pass

# zhangsan = NvPengYou('女','183cm','90kg','锡纸烫','32岁')
# zhangsan.work()

'''
类的重写/多态
'''
# class NvPengYou(GirlFriend):    #在括号里面输入被继承的类。于是它就获得了继承的方法等等. 一个是父类；一个是子类；
#     def work(self) :
#         print('修电脑') #类的重写，work改为了：“修电脑”


# --------------------------------------------------------------------------------------------------------------------------------
import time



'''
python 的常见技巧科普
'''
'''
文件的读写
# '''
# now = time.strftime('%y-%m-%d %H:%M:%S')

# text = input('请输入今天的心情：')
# with open('日记.txt','a',encoding = 'utf8') as f :  #文件路路径（可以绝对路径，也可以相对路径）以及文件名，w写入（a追加）（r读取），编码是utf8
#     f.write(now+'\n')
#     f.write(text+"\n")
#     f.write('-------------------\n')

'''
python的制表符
\t  #空格
\n  #换行
'''
'''
关于时间
'''




