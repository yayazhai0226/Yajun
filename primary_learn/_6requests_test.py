"""
自动化测试是什么？
一、UI自动化测试（模拟执行功能测试的过程，也就是模拟点点点）
    web
    app
    1代码（学了代码，再去使用工具）（可根据现有系统情况，定制自己的自动化测试工具）
二、接口自动化测试
        requests
            步骤
                1构造请求
                2判断结果
                    HTTP状态码(接口能否正常工作)
                    接口返回值（接口功能是否有问题）
                    数据库查询（确认返回数据正确）
            请求
                get
                post
                request
            常用方法
                res.test(打印返回值)
                res.status_code(打印状态码)
            断言

            二次封装 
    2工具
        postman
        jmeter
        httprunner
""" 

"""
requests
pip install requests
可以用postman里的代码，来使用requests包
"""
import requests
from _0dbtools  import Db

# url = "http://47.105.178.190:2333/login"  #post接口
# headers = {"Content-Type":"application/json"}
# data = {"username":"yayazhai0226","password":"12345678"}    

# res = requests.post(url = url,headers = headers,json = data)    #获得了所有返回结果
# print(res.text) #只取了返回结果中的有用的text

# url = "http://47.105.178.190:2333/showversion"    #get类型接口
# headers = {"Content-Type":"application/json"}
# res = requests.get(url = url,headers = headers)
# print(res.text)

# url = "http://47.105.178.190:2333/regist"
# headers = {"Content-Type":"application/json"}
# data = { "username":"yanquu", "password":"12345678",  "phone":"15196910085",  "email":"845671609@qq.com"  }
# res = requests.post(url = url,headers = headers,json = data)
# print(res.text) #text以字符串/文本的显示格式

# res1 = res.json()   #获得的数据类型是：字典
# # print(type(res1))
# status = res1.get("status")
# if status == 200:
#     print("注册成功！测试通过！")
# else:
#     print("注册失败")

# db = Db("47.105.178.190","root","123456","ljtestdb")

# url = "http://47.105.178.190:2333/get_title_img"
# res = requests.get(url = url) 
# data = res.json().get("data")
# num = len(data)
# res = db.chaxun("select count(*) from t_title_img where status = 0;")[0][0]
# # print(res)
# if num == res:
#     print("测试通过！")
# else:
#     print("测试失败！")



"""
某业务流程：登录——写文章——修改文章
"""
"""
请求头  请求主题  响应主体
"""
"""
断言在自动化中很常用：assert
断言通过=登录成功
断言失败=登录失败

"""
"""
1、登录
"""
# import requests

# url = "http://47.105.178.190:2333/login"
# data = {"username":"yayazhai0226","password":"12345678"}
# res = requests.post(url = url,json = data)  #返回的是json格式
# # r = res.json()   #把结果转换成字典
# # r = res.status_code #获取http状态码
# assert res.status_code == 200   #如果断言通过，继续执行
# assert res.json()["status"] == 200  
# token = res.json()["data"]["token"]

"""
以上的断言就是，代替了  if else 的方法，这样更加好用！
"""
# if res.status_code == 200:
#     if res.json()["status"] == 200:
#         print("登录成功!")
#     else:
#         print("登录失败")
# else:
#     print(res.status_code)
#     print("接口挂了！")

"""
2、写文章
"""
# url = "http://47.105.178.190:2333/article/new"
# data = { "title":"今天在python发了一篇文章",  "content":"哈哈，如图",  "tags":"测试",  "brief":"介绍",  "ximg":"dsfsdf.jpg"  }
# headers = {"token":token}
# res = requests.post(url = url,json = data,headers = headers)
# assert res.status_code == 200
# assert res.json()["status"] == 200
"""
3、修改文章
"""
# url = "http://47.105.178.190:2333/article/update"
# data = { "title":"测试入门容易，高精尖难", "content":"是啊",  "tags":"君子",  "brief":"可爱", "ximg":"dsfsdf.jpg", "aid":1}
# headers = {"token":token}
# res = requests.post(url = url,json = data,headers = headers)
# assert res.status_code == 200
# assert res.json()["status"] == 200
# print("修改文章成功")



"""
为了实现接口自动化测试，第一步就是把方法弄出来！（核心！！！）
封装方法
request() 方法
"""

def request(method,url,jsondata = {},headers = {},httpcode = 200,aresult = 200):
    res = requests.request(method,url = url,json = jsondata,headers = headers)  
    try:
        assert httpcode == res.status_code
        assert aresult == res.json()["status"]
        return res.text
    except:
        return res.text
method = "get"
url ="http://47.105.178.190:2333/login"
jsondata = {"username":"yayazhai0226","password":"12345678"}
r = request(method,url,jsondata)
print(r)


"""
txt
csv #也是一个表格，不太好用
exel
mysql
"""

"""
1. 测试用例放到excel，单个接口
2. 读取出来
3. 再去循环执行测试用例
"""






