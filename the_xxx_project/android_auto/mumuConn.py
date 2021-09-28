#作者：zengziwei
#创建时间：2021/8/13 18:02
#文件名：mumuConn.py

from appium import webdriver
import time
import os

# 配置参数
desired_cap={}
# 设备信息
desired_cap["platformName"] ="Android"
desired_cap["platformVersion"]="6"
desired_cap["deviceName"]= "mumu"
desired_cap["appPackage"] = "com.xykj.mall"
desired_cap["appActivity"]="com.wjxls.mall.ui.activity.main.MainActivity"

# 声明手机驱动对象
d = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
time.sleep(15)

cur_file=os.curdir
pathname=cur_file+ '/login_img'
if not os.path.exists(pathname):
    os.makedirs(pathname)

d.save_screenshot(pathname+"/homePage.png")

# 定位元素
d.find_element_by_name("我的").click()
time.sleep(10)

d.find_element_by_id("com.xykj.mall:id/et_fragment_login_register_account_login_phone").send_keys("XXXXXXXXXXXX")
time.sleep(2)
d.find_element_by_id("com.xykj.mall:id/et_fragment_login_register_account_login_phone_password").send_keys("123456")
time.sleep(2)
d.save_screenshot(pathname+"/accountPwd.png")

d.find_element_by_id("com.xykj.mall:id/bt_fragment_login_register_account_login_tologin").click()
time.sleep(2)

d.find_element_by_name("我的").click()
time.sleep(4)
d.save_screenshot(pathname+"/personalPage.png")

d.find_element_by_id("com.xykj.mall:id/csl_fragment_persen_center_user_header_layout").click()
time.sleep(2)
d.save_screenshot(pathname+"/userInfoPage.png")
# 切换账号
# d.find_element_by_id("com.xykj.mall:id/ll_account_manage_switch_account").click()
# time.sleep(2)

#退出登录
d.find_element_by_id("com.xykj.mall:id/account_manage_activity_tv_sign_out").click()
time.sleep(2)
d.save_screenshot(pathname+"/outline1.png")

d.find_element_by_id("com.xykj.mall:id/bt_dialog_common_twobutton_right").click()
d.save_screenshot(pathname+"/outline2.png")
# 关闭驱动对象同时关闭其他应用
d.quit()
