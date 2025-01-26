# 测试在删除标签弹窗中，是否可以删除标签
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

def test_page_0333():

    #进入标签页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("标签")').click()
    time.sleep(8)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("管理")').click()
    time.sleep(8)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("test")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/ctd').click()
    time.sleep(8)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除")').click()
    time.sleep(8)
    driver.find_element(AppiumBy.ID, 'com.tencent.mm:id/actionbar_up_indicator_btn').click()
    time.sleep(10)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0333.png')


    try:
         # 断言新建标签页面元素
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("test")')
        assert False, "Element should not exist on the page."

    except NoSuchElementException:
        pass
        # 测试通过，如果成功取消搜索
        print("test pass")

    time.sleep(1)

    driver.quit()

if __name__ == '__main__':
    pytest.main()

