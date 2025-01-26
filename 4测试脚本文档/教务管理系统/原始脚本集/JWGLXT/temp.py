import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建ChromeOptions对象
chrome_options = webdriver.ChromeOptions()

# 禁用图形加速
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://120.26.37.204:8081')
driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,'email').send_keys('8001@qq.com')
time.sleep(3)
driver.find_element(By.NAME,'password').send_keys('0123456')
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'请假申请').click()
time.sleep(3)
driver.find_element(By.NAME,'leave_date').send_keys('0098')
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[2]/button').click()
time.sleep(3)
time.sleep(3)

driver.quit()

