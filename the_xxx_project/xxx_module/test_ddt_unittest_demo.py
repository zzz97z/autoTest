#作者：zengziwei
#创建时间：2021/8/13 11:51
#文件名：test_ddt_unittest_demo.py
from ddt import unpack,data,ddt
import unittest
from public_method.requests_json import *
from public_method.excel_read import get_xl
import json
@ddt
class Test(unittest.TestCase):
    # 选择文件读取
    test_data = get_xl("D:\pythonScript\interface_auto_test\data\demo.xls","Sheet1")
    @data(*test_data)
    @unpack
    def test_a(self,url,method,header,body):
        lg=request_port(url,method,json.loads(header),json.loads(body)).request_post()
        self.mg=lg.json()['status']
        param=lg.json()['params']
        if self.mg==200:
            res='PASS'
            print(res)
        else:
            res='FAIL'
            print('')
            self.assertEquals(self.mg,200,msg='\n{}\n{}'.format(res,param,self.mg))

if __name__ == '__main__':
    unittest.main()