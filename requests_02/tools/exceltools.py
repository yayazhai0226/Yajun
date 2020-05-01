import xlrd

def read_excel(excel_path,sheet_name,skip_first = True):
    """
        方法：读取excel
        参数：
            excel_path:
            sheet_name:
            skip_first:
        返回值：[[row1],[row2]...]

    """
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first is True:
        start_row = 1
    else:
        start_row = 0

    for row in range(start_row,table.nrows):
        results.append(table.row_values(row))
    return results



if __name__ == "__main__":
    path = "G:\\workhome\\Yajun_learn\\Yajun\\requests_02\\case\\测谈网测试用例test.xlsx"
    sheet_name = "Sheet1"
    for a in read_excel(excel_path=path,sheet_name=sheet_name):
        print(a)
     