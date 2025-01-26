import os
import time
import unittest
from io import BytesIO

import pytest
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#验证会员账号不存在对应会员是否会给出提示
def test_page_0076():
    # 初始化WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 打开登录页面
    driver.get('http://120.26.37.204:8088/marks/login/')

    #登录
    driver.find_element(By.NAME, "userName").send_keys("saler11")
    time.sleep(1)
    driver.find_element(By.NAME, "passWord").send_keys("0123456")
    time.sleep(1)
    driver.find_element(By.ID, "loginFormBtn").click()
    time.sleep(2)

    #会员信息查看页面
    driver.find_element(By.LINK_TEXT, "会员信息查看").click()
    time.sleep(2)

    #定位会员账号
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/input").send_keys("666")
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[3]/button").click()
    time.sleep(2)

    #测试截屏
    driver.save_screenshot('CSGLXT_CSYL_0076.png')

    #判断预期结果
    result = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div")
    assert "未找到相关内容" in result.text, "测试失败"
    print("测试成功")

if __name__ == '__main__':
    pytest.main()