
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

def test_page_0272():

    #进入仅聊天的朋友页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("仅聊天的朋友")').click()
    time.sleep(8)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("移出")').click()
    time.sleep(3)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("朋友1")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ID, 'com.tencent.mm:id/fp').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("移出")').click()
    time.sleep(5)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0272.png')

    try:
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("朋友1")')
        assert False, "Element should not exist on the page."

    except NoSuchElementException:
        pass
        # 测试通过，如果成功移出朋友
        print("test pass")

    time.sleep(2)


    driver.quit()

if __name__ == '__main__':
    pytest.main()

