import requests
from tools.requeststools import request

url = "http://192.144.148.91:2333/login"
data = {"username":"yayazhai0226","password":"a1234567"}
headers = {"Content-Type":"application/json"}

r = request("post",url =url,data = data,headers = headers)
print(r)





