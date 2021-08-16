#作者：zengziwei
#创建时间：2021/8/13 11:01
#文件名：from_sql_get_xxx.py
from public_method.sql_conn_operation import Mysql
from public_method.sql_config import getConfig
from itertools import chain
class do_sql():
    def __init__(self):
        self.db_link="xxx1_project"
        self.db_host=getConfig(self.db_link,"dbhost")
        self.db_name=getConfig(self.db_link,"dbname")
        self.db_account=getConfig(self.db_link,"dbuser")
        self.db_pwd=getConfig(self.db_link,"dbpassword")
        self.db_port=getConfig(self.db_link,"dbport")
        # print(self.db_host,self.db_account,self.db_pwd,self.db_name,self.db_port)
        self.conn=Mysql(self.db_host,self.db_account,self.db_pwd,self.db_name,self.db_port)
        self.id=2
    def get_token(self):
        sql='select token from user where id={}'.format(self.id)
        tok=self.conn.find_all()
        res=list(chain.from_iterable(tok))
        return res