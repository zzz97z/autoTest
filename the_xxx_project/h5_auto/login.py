#作者：zengziwei
#创建时间：2021/8/13 16:10
#文件名：mumuConn.py
import time
from selenium import webdriver
import os
# 设置截图保存路径
cur_file=os.curdir
pathname=cur_file+ '/login_img'
if not os.path.exists(pathname):
    os.makedirs(pathname)

driver = webdriver.Chrome()
driver.set_window_size(180, 1000)

url='http://xykj2.test.meetlan.com'
driver.get(url)
time.sleep(2)

driver.get_screenshot_as_file(pathname+'/HomePage.png')

driver.find_element_by_xpath('//*[@id="footer"]/div[3]').click()
time.sleep(2)



driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div[1]').click()
time.sleep(2)

driver.get_screenshot_as_file(pathname+'/loginPage.png')

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[2]/form/div[1]/div/input').send_keys('XXXXXXX')
time.sleep(2)


driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[2]/form/div[2]/div/input').send_keys('123456')
time.sleep(2)

driver.get_screenshot_as_file(pathname+'/AccountPasswordLogin.png')

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[5]').click()
time.sleep(2)

driver.get_screenshot_as_file(pathname+'/PersonalPage.png')

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[1]').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div[2]/div[2]/div[2]').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]').click()
time.sleep(2)



driver.quit()

