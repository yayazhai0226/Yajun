import requests

def save_token(data):
    """
        获得token，并存为全局变量
    """
    try:
        token = data.get("data").get("token")
        globals()["token"] = token
        # print(token)
    except:
        # print("没有发现token")
        pass
def get_token():
    if globals().get("token") != None:
        return globals()["token"]
    else:
        return ""

def request(method,url,data,headers = {},httpcode = 200,aresult = 200):
    """
        名称：
            请求
        参数：
            url：地址   
            method：请求的类型
            jsondata：json的参数
            headers:请求头
        返回值：
            True
            False
    """
    res = requests.request(method,url = url,json = data ,headers = headers)
    save_token(res.json())
    try:
        assert httpcode == res.status_code
        assert aresult == res.json()["status"]
        return True
    except:
        return False
    


