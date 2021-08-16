#作者：zengziwei
#创建时间：2021/8/13 11:07
#文件名：runReport.py
# coding=utf-8
import unittest
import HTMLTestRunner_cn
import time
import os

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
case_path = os.path.join(curpath)

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    get_time = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    htmlreport = reportpath+r"\{}_result.html".format(get_time)
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")

    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)