import requests


def save_token(data):
    """
        使用全局变量保存token
    """
    try:
        token = data.get("data").get("token")
        globals()["token"] = token
    except:
        # print("没有发现token，不用保存")
        pass
        
def get_token():
    """
        获取token
    """
    if globals().get("token") != None:
        return globals()["token"]
    else:
        return ""

def request(method, url, jsondata={}, headers={}, httpcode=200, aresult=200):
    """
        名称：
            请求核心引擎
        参数：
            url：地址
            method：请求的方法
            jsondata：json格式的参数
            headers：请求头
        返回值：
            true：通过
            false：失败
    """
    res = requests.request(method, url=url, json=jsondata, headers=headers)
    save_token(res.json())
    try:
        assert httpcode == res.status_code
        assert aresult == res.json()["status"]
        return True
    except:
        # print(res.text)
        return False