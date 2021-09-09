#作者：zengziwei
#创建时间：2021/9/9 13:56
#文件名：GET_LOG.py
import os
import time
def get_log(title,result,params):
    cur_dir = os.curdir
    cur_time=time.strftime('%Y_%m_%d')
    log_time=time.strftime('%Y_%m_%d %H:%M:%S')
    new_dir=cur_dir+'/log'
    path=new_dir+'/{}_{}_log.txt'.format(cur_time,title)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    ft = open(path, 'a', encoding='utf-8')
    print(f'{log_time}\tINFO', f'开始执行{title}测试用例...', file=ft)
    print(f'{log_time}\tINFO', '开始执行用例...' ,file=ft)
    print(f'{log_time}\tINFO', '入参是{}'.format(params), file=ft)
    print(f'{log_time}\tINFO', '用例结果是{}...'.format(result), file=ft)
    print("-----------------------------------------", file=ft)
    ft.close()