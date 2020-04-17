import requests

#1.登录
url = "http://192.144.148.91:2333/login"
data = {"username":"liuyun1", "password":"a12345678"}
res = requests.post(url=url, json=data)
assert res.status_code == 200 # 如果断言通过，就那继续往下执行，反之报错。
assert res.json()["status"] == 200
token = res.json()["data"]["token"]
print("登录成功了")

#2.写文章
url = "http://192.144.148.91:2333/article/new"
data = {"title":"123", "content":"123埃里克的是解放拉萨的","tags":"测试", 
"brief":"三生三世", "ximg":"dsfsdf.jpg"}
headers = {"token":token}
res = requests.post(url=url, json=data, headers=headers)
assert res.status_code == 200 # 如果断言通过，就那继续往下执行，反之报错。
assert res.json()["status"] == 200
aid = res.json()["data"]["articleid"]
print("写文章成功了！")

#3.修改文章
url = "http://192.144.148.91:2333/article/update"
data = {"title":"为什么要学习测试","content":"内容","tags":"测试",
"brief":"介绍","ximg":"dsfsdf.jpg","aid":aid}
headers = {"token":token}
res = requests.post(url=url, json=data, headers=headers)
assert res.status_code == 200 # 如果断言通过，就那继续往下执行，反之报错。
assert res.json()["status"] == 200
print("修改文章成功了")