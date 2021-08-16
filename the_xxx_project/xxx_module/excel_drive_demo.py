#作者：zengziwei
#创建时间：2021/8/13 11:09
#文件名：excel_drive_demo.py
import xlrd
from public_method.requests_json import *
from xlutils import copy
import json

path = 'D:\pythonScript\interface_auto_test\data\demo.xls'
wb = xlrd.open_workbook(path)
new_wb = copy.copy(wb)

wb_sheet = wb.sheet_by_name('Sheet1')
nrows = wb_sheet.nrows
ncols = wb_sheet.ncols
new_sheet = new_wb.get_sheet(1)
row = 1
environment = 'http://localhost:8080'
for i in range(nrows - 1):
    url = wb_sheet.cell_value(row, 0)
    method = wb_sheet.cell_value(row, 1)
    headers = wb_sheet.cell_value(row, 2)
    body = wb_sheet.cell_value(row, 3)
    res = request_port(environment + url, method, json.loads(headers), json.loads(body)).request_post()
    res_data = res.json()
    status = res.json()['status']
    mg = res.json()['msg']
    if status == 200:
        new_sheet.write(row, ncols - 3, 'PASS')
        new_sheet.write(row, ncols - 2, str(mg))
        new_sheet.write(row, ncols - 1, str(res_data))
    else:
        new_sheet.write(row, ncols - 3, 'FAIL')
        new_sheet.write(row, ncols - 2, str(mg))
        new_sheet.write(row, ncols - 1, str(res_data))
    row += 1
new_wb.save(path)