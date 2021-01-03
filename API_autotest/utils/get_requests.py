import requests

# 封装Get方法
def requests_get(url ,headers) :
    r = requests.get(url,headers = headers) #发起请求
    code = r.status_code    #获取结果响应内容
    try :
        body = r.json()
    except Exception as e :
        body = r.text
    res = dict()    #内容存到字典
    res['code'] = code
    res['body'] = body
    return res  #字典返回