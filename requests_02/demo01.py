import requests

#构造请求(get请求/post请求)
# url = "http://192.144.148.91:2333/get_title_img"
# res = requests.get(url)
# print(res.text)

#登录
url = "http://192.144.148.91:2333/login"
data = {"username":"yayazhai0226","password":"a1234567"}
res = requests.post(url = url,json = data)
assert res.status_code == 200
assert res.json()["status"] == 200
token = res.json()["data"]["token"]
print("登录成功")

#写文章
url = "http://192.144.148.91:2333/article/new"
data = { "title":"我是翟，我在写文章","content":"感谢你的浏览","tags":"测试帅哥","brief":"介绍一下"}
headers = {"token":token}
res = requests.post(url = url,json = data,headers = headers)
assert res.status_code == 200
assert res.json()["status"] == 200
aid = res.json()["data"]["articleid"]
print("写文章成功")

#修改文章
url = "http://192.144.148.91:2333/article/update"
data = {"title":"我是翟，我在改文章", "content":"内容", "tags":"测试帅哥", "brief":"介绍一下","aid":aid}
headers = {"token":token}
res = requests.post(url = url,json = data,headers = headers)
assert res.status_code == 200
assert res.json()["status"] == 200
print("修改文章成功")

#删除文章
url = "http://192.144.148.91:2333/article/delete"
data = {"aid":aid}
headers = {"token":token}
res = requests.post(url = url,json = data,headers = headers)
assert res.status_code == 200
assert res.json()["status"] == 200
print("删除文章成功")

