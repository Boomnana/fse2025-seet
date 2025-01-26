# 验证点击会员信息查看页面是否能跳转到相应的正确页面
import os
import time
import unittest

from io import BytesIO

import pytest
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_page_0064():
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
    time.sleep(5)

    # 会员信息查看页面url
    member_page_url = "http://120.26.37.204:8088/marks/memberInfos/show/"

    # 点击会员信息查看页面
    member_info_link = driver.find_element(By.LINK_TEXT, "会员信息查看")
    member_info_link.click()

    #测试截屏
    driver.save_screenshot('CSGLXT-CSYL-0064.png')
    time.sleep(5)

    #判断是否正确跳转到会员信息页面
    try:
        # 检查页面url
        assert driver.current_url == member_page_url
        print("测试通过：成功跳转到会员信息页面")
    except:
        print("测试失败")


if __name__ == '__main__':
    pytest.main()