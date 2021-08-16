#作者：zengziwei
#创建时间：2021/8/13 10:56
#文件名：sql_conn_operation.py
import pymysql
class Mysql():
    def __init__(self,host,user,paw,db,port):
        """链接数据库的基本信息"""
        self.host=host
        self.user=user
        self.paw=paw
        self.db_name=db
        self.port=port
        self.db = pymysql.connect(host=self.host,user=self.user,password=self.paw,db=self.db_name,port=self.port)

    def find_all(self,sql):
        """返回当前sql语句查询到的所有数据"""
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 使用 fetchone() 方法获所有数据.
        data = cursor.fetchall()
        # 关闭数据库连接
        cursor.close()
        self.db.close()
        return data

    def find_one(self,sql):
        """返回当前sql语句查询到的单行数据"""
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 使用 fetchone() 方法获所有数据.
        data = cursor.fetchone()
        # 关闭数据库连接
        self.db.close()
        return data

    def execute_sql(self,sql):
        """支持增、删、改sql语句"""
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            self.db.commit()
            return True
        except Exception as msg:
            # 发生错误时回滚
            self.db.rollback()
            print("执行失败：%s"%msg)



if __name__=="__main__":
    Mysql()