import requests

class Utiles() :
    def __init__(self) :
    #重构get和post方法
        #定义公共方法
        #增加cookies headers 参数
        #根据参数method判断get/post请求
    def requests_api(self, url , data = None , json = None , headers = None , cookies = None , method = 'get') :
        if method == 'get' :
            self.log.debug('发送get请求')
            r = requests.get(url , data = data , json = json , headers = headers , cookies = cookies)
        elif method == 'post' :
            self.log.debug('发送post请求')
            r = requests.post(url , data = data , json = json , headers = headers , cookies = cookies)
        code = r.status_code    #获取结果响应内容
        try :
            body = r.json()
        except Exception as e :
            body = r.text
        res = dict()    #内容存到字典
        res['code'] = code
        res['body'] = body
        return res  #字典返回


    # 重构GET方法
    def get(self , url , **kwargs) :
        return self.requests_api(url , menthod = 'get' , **kwargs)

    #重构post方法
    def post(self , url , **kwargs) :
        return self.requests_api(url , method = 'post' , **kwargs)




