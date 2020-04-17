"""
    读写excel
"""

import xlrd

# 读取excel的方法
def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法：读取excel
        参数：
            excel_path: excel的文件路径
            sheet_name: 要读取的excel的sheet名字
            skip_first: 是否跳过首行，默认跳过
        返回值：[[row1], [row2], [row3]....]
    """
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first is True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的信息
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results

    

# 只在当前的py文件中运行，才去执行它的代码
if __name__ == "__main__":
    path = 'C:\\Users\\SNake\\VSCodeProjects\\ljtest202003\\RequestTest\\case\\测谈网接口测试用例.xlsx'
    sname = "Sheet1"
    for a in read_excel(path, sname):
        print(a)