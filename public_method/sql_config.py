#作者：zengziwei
#创建时间：2021/8/13 11:02
#文件名：sql_config.py
import configparser
#
# #获取config配置文件
def getConfig(section, key):
    config = configparser.ConfigParser()
    path = "D:\pythonScript\interface_auto_test\data\sql.conf"
    config.read(path)
    return config.get(section, key)