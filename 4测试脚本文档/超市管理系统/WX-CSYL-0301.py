# 测试是否成功新建标签
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
from selenium.common import NoSuchElementException
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

def test_page_0301():
    #进入标签页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("标签")').click()
    time.sleep(10)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("新建")').click()
    time.sleep(3)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/d98').send_keys('test')
    time.sleep(3)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/kao').click()
    time.sleep(10)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0301.png')

    try:
        # 断言新建标签页面元素
        tap_page_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("当前标签无成员")')
        assert tap_page_element.is_displayed()
        time.sleep(5)
        print("test pass")

    except Exception as e:
        # 测试失败
        print("test failed: ", e)

    time.sleep(1)

    driver.quit()

if __name__ == '__main__':
    pytest.main()

