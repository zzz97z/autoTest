# 作者：zengziwei
# 创建时间：2021/8/13 10:56
# 文件名：sql_conn_operation.py

import pymysql
class Mysql:
    def __init__(self, db_link, db_user, db_password, db_name, db_port):
        self.db_link = db_link
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.db_port = db_port
        self.db_conn = pymysql.connect(host=self.db_link, user=self.db_user, password=self.db_password,
                                       db=self.db_name, port=self.db_port)

    def find_all(self, sql):
        cursor = self.db_conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self.db_conn.close()
        return data

    def find_one(self, sql):
        cursor = self.db_conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        self.db_conn.close()
        return data

    def del_add_up_sql(self, sql):
        cursor = self.db_conn.cursor()
        try:
            cursor.execute(sql)
            self.db_conn.commit()
        except Exception as msg:
            self.db_conn.rollback()
            print(msg)

if __name__ == "__main__":
    conn = Mysql('db_link', 'db_user', 'db_password', 'db_name', 3306)
    sql = 'select * from m_user'
    res = conn.find_all(sql)
    print(res)
