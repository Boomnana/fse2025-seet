# 测试在搜索状态下，点击取消按钮是否能退出搜索状态并恢复到正常页面
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

def test_page_0227():
    #进入添加手机联系人页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("新的朋友")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("添加手机联系人")').click()
    time.sleep(8)
    #点击搜索按钮
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/jgr').click()
    time.sleep(8)
    #推出搜索页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("取消")').click()
    time.sleep(5)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0227.png')

    #判断预期结果
    try:
        phone_contacts_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("查看手机通讯录")')
        assert phone_contacts_element.is_displayed()
        time.sleep(1)
        # 测试通过，如果成功取消搜索
        print("test pass")

    except:
        # 测试失败
        print("test failed ")

    time.sleep(1)


    driver.quit()

if __name__ == '__main__':
    pytest.main()