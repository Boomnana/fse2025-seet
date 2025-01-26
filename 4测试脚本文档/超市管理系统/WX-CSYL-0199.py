# 测试用户通过搜索手机号搜索相关用户的功能是否成功
import os
import time
import unittest
from io import BytesIO
from telnetlib import EC

import pytest
from PIL import Image
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


# 设定Appium的Desired Capabilities
options = UiAutomator2Options()
options.load_capabilities({
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'noReset': True
})
# 初始化WebDriver
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(10)

def test_page_0199():

    #进入添加朋友页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("新的朋友")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("添加朋友")').click()
    time.sleep(5)

    #点击搜索
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/mes').click()
    time.sleep(2)
    # 搜索已添加的朋友
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("账号/手机号")').send_keys('18066238395')
    time.sleep(3)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("搜索:18066238395")').click()
    time.sleep(10)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0199.png')

    try:
        add_friend_message = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("发消息")')
        assert add_friend_message.is_displayed()
        time.sleep(1)
        # 测试通过，如果进入朋友页面
        print("test pass")

    except Exception as e:
        # 测试失败
        print("test failed: ", e)

    time.sleep(1)

    driver.quit()

if __name__ == '__main__':
    pytest.main()