#作者：zengziwei
#创建时间：2021/8/13 10:56
#文件名：requests_json.py
import requests
import json
class request_port():
    def __init__(self,url,method,header,data):
        self.url = url
        self.method = method
        self.header = header
        self.data = data
    def request_post(self):
        #判断
        if self.method == "post":
            response = requests.post(url=self.url, headers=self.header, data=json.dumps(self.data))
        else:
            response = requests.get(url=self.url, headers=self.header)
        return  response