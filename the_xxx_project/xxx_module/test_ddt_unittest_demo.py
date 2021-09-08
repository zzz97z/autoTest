#作者：zengziwei
#创建时间：2021/8/13 11:51
#文件名：test_ddt_unittest_demo.py
from ddt import unpack,data,ddt
import unittest
from public_method.requests_json import *
from public_method.ex_operation import xl_operation
import json
@ddt
class Test(unittest.TestCase):
    # 选择文件读取
    test_data = xl_operation().xls_get("D:\pythonScript\interface_auto_test\data\demo.xls","Sheet1")
    @data(*test_data)
    @unpack
    def test_a(self,caseId,url,method,header,body):
        lg=request_port(url,method,json.loads(header),json.loads(body)).request_post()
        self.mg=lg.json()['status']
        param=lg.json()['params']
        if self.mg==200:
            res='PASS'
            xl_operation().xls_upadate("D:\pythonScript\interface_auto_test\data\demo.xls",caseId,6,res)
        else:
            res='FAIL'
            xl_operation().xls_upadate("D:\pythonScript\interface_auto_test\data\demo.xls", caseId, 6, res)
            self.assertEquals(self.mg,200,msg='\n{}\n{}'.format(res,param,self.mg))

if __name__ == '__main__':
    unittest.main()