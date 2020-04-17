"""
    运行入口
"""
from tools.exceltools import read_excel
from tools.requeststools import request
from tools.requeststools import get_token
import xlrd
import xlutils

base_url = "http://47.105.178.190:2333"         # 所有接口ip地址和端口号
sheet_name = 'Sheet1'                           # excel的Sheet名字
excel_path = 'case\\测谈网接口测试用例.xlsx'     # excel路径名字

res = read_excel(excel_path, sheet_name)        # 把所有接口取出来，存到res变量里面 [[row1], [row2], ..]

# 循环的取每一行
for r in res:           # r当前的哪一行
    # 取值
    case_name = r[1]
    case_method = r[3]
    case_http_code = r[6]
    case_result_code = r[7]
    case_headers = eval(r[5])
    case_url = base_url + r[2]
    case_headers["token"] = get_token()

    try:
        case_data = eval(r[4])
    except:
        case_data = {}

    # 请求 rsp就是执行的结果：true成功，false失败
    rsp = request(case_method, case_url, case_data, case_headers, case_http_code, case_result_code)
    if rsp is True:
        print("测试用例【{}】执行通过".format(case_name))
    else:
        print("测试用例【{}】执行失败".format(case_name))

"""
from xlutils.copy import copy        #导入copy模块
rb = xlrd.open_workbook(excel_path)    #打开.xls文件
wb = copy(rb)                          #利用xlutils.copy下的copy函数复制
ws = wb.get_sheet(0)                  #获取表单0
ws.write(0, 0, 'changed!')             #改变（0,0）的值s
ws.write(0,1,label = '好的')           #增加（8,0）的值
wb.save(sheet_name)                    #保存文件
"""






