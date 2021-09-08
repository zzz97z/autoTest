#作者：zengziwei
#创建时间：2021/9/7 18:42
#文件名：ex_operation.py
import xlrd
import xlwt
from xlutils import copy
class xl_operation:
    #新建空白文件
    def xls_add(self,path, sheetName):
            wb = xlwt.Workbook(encoding='utf-8')
            sheet = wb.add_sheet(sheetName)
            wb.save(path)
    #修改文件
    def xls_upadate(self,path, row, col, value):
            wb = xlrd.open_workbook(path)
            new_wb = copy.copy(wb)

            new_sheet = new_wb.get_sheet(0)

            new_sheet.write(row, col, value)
            new_wb.save(path)
    def xls_clear(self):
        pass
    #获取数据为字典形式
    def xls_get(self,filePath,sheet_name):
        wb=xlrd.open_workbook(filePath,'r')
        Sheet=wb.sheet_by_name(sheet_name)
        nrows=Sheet.nrows
        #获取键
        k=Sheet.row_values(0)
        #获取值
        res=[]
        for i in range(1,nrows):
            a=Sheet.row_values(i)
            dict_k_v=dict(zip(k,a))
            res.append(dict_k_v)
        return res

if __name__ == '__main__':
    a=xl_operation()
    res=a.xls_get('D:\pythonScript\demo\www.xls','Sheet1')
    print(res)