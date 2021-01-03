import requests
def requests_post(url,json = None , headers = None) :
    r = requests.post(url , json = json , headers = headers)
    code = r.status_code
    try :
        body = r.json 
    except Exception as e :
        body = r.text

    res = dict()
    res['code'] = code
    res['body'] = body
    return res