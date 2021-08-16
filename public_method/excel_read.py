#作者：zengziwei
#创建时间：2021/8/13 10:57
#文件名：excel_read.py

import xlrd
def get_xl(file,sheetName):
    wb=xlrd.open_workbook(file)

    # 找表
    Sheet=wb.sheet_by_name(sheetName)

    # 获取表的行数
    nrows=Sheet.nrows

    # 遍历表格
    test_data = []
    for i in range(1, nrows):
        a = Sheet.row_values(i)
        test_data.append(list(a))
    return test_data