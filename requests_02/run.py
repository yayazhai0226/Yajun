"""
    运行入口 
"""
from tools.exceltools import read_excel
from tools.requeststools import request
from tools.requeststools import get_token

sheet_name = "Sheet1"
base_url = "http://192.144.148.91:2333"
excel_path = "case\\测谈网测试用例test.xlsx"
res = read_excel(excel_path,sheet_name)
for r in res:
    case_name = r[1]
    case_method = r[3]
    case_aresult = r[7]
    case_http_code = r[6]
    case_url = base_url+r[2]
    case_headers = eval(r[5])
    case_headers["token"] = get_token()
    try:
        case_data = eval(r[4])
    except:
        case_data = {}
    rs = request(case_method, case_url,case_data,case_headers,case_http_code,case_aresult)
    if rs is True:
        print("测试用例【{}】执行通过".format(case_name))
    else:
        print("测试用例【{}】执行失败".format(case_name))
    print("---------------------------------------------------")







