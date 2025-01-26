import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time

class WeChatGroupChatNameTest(unittest.TestCase):
    def setUp(self):
        # 初始化Appium WebDriver
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:5554',  # 确保这是你的设备或模拟器的正确地址
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            # 可能还需要添加其他配置，如自动化名称、新命令超时等
        }

        options = UiAutomator2Options().load_capabilities(desired_caps)
        # 初始化Appium WebDriver
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

        time.sleep(10)

    def tearDown(self):
        # 关闭WebDriver
        self.driver.quit()

    """测试用例WX-CSYL-0611:验证系统是否提供了输入相同数字的功能界面；"""
    def test_group_chat_name_change(self):
        # 点击左上方的+号
        plus_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '更多功能按钮')
        plus_button.click()
        time.sleep(5)

        # 选择“发起群聊”并点击进入
        FQQL = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发起群聊")')
        FQQL.click()
        time.sleep(5)

        # 点击面对面建群
        group_name = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("面对面建群")')
        group_name.click()
        time.sleep(5)

        # 验证系统是否提供了输入相同数字的功能界面；
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/dpb")))

        print("测试用例通过：系统提供了输入相同数字的功能界面。")


if __name__ == '__main__':
    unittest.main()