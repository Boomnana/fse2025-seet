# 测试是否能够从新的朋友页面成功跳转到添加朋友页面
import os
import time
from io import BytesIO

import pytest
from PIL import Image
from _pytest import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import unittest

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

def test_page_0181():
    #进入添加朋友页面
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通讯录")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("新的朋友")').click()
    time.sleep(5)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("添加朋友")').click()
    time.sleep(5)

    # 测试截屏
    driver.save_screenshot('WX_CSYL_0181.png')

    #判断预期结果
    try:
        add_friend_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("添加朋友")')
        assert add_friend_element.is_displayed()
        time.sleep(1)
        # 测试通过，如果添加朋友页面成功加载
        print("test pass")

    except Exception as e:
        # 测试失败
        print("test failed: ", e)

        time.sleep(1)

    #关闭app
    driver.quit()

if __name__ == '__main__':
    pytest.main()



