
import  requests

# 登录用例脚本
url = 'https://www.baidu.com/'
data = {'username':'test123','password':'12345678'}
r = requests.post(url, json = data)

# 编写个人信息获取脚本
url = "http://127.0.0.1:8080/user/"
headers = '{"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjUwNjMwOTksInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsInVzZXJuYW1lIjoicHl0aG9uIn0.f3GdeSnzb3UGs-w1p1ejZ1rNLaaiBOAHUnN8_pq8LDE"}'
r = requests.get(url , headers = headers)

# 商品列表数据
url = 'https://www.baidu.com/'
data = {'page':'1','page_size':'10','ordering':'create_time'}
r = requests.get(url,json = data)

# 添加到购物车
def cart():
    url = 'https://www.baidu.com/'
    data = {'sku_id':'3','count':'1','selected':'true'}
    headers = {'Authorization':'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjU4NTU2NzcsInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsInVzZXJuYW1lIjoicHl0aG9uIn0.yotHV8wMX7MKHyioFDaGnrjTDTAYsLB0R8Qsungw_ms'}
    r = requests.post(url,json = data , headers = headers)

#保存订单
def orders():
    url = 'http://127.0.0.1:8080/orders/'
    data = {'address':'1','pay_method':'1'}
    headers = {'Authorization':'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjU4NTU2NzcsInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsInVzZXJuYW1lIjoicHl0aG9uIn0.yotHV8wMX7MKHyioFDaGnrjTDTAYsLB0R8Qsungw_ms'}
    r = requests.post(url , json = data , headers = headers)
    




