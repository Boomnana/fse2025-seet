import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time

class WeChatTestCase(unittest.TestCase):
    def setUp(self):
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

    """测试用例WX-CSYL-0564:验证用户能否通过搜索找到特定联系人"""
    def test_create_group_chat_and_search(self):
        # 点击左上方的+号
        plus_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '更多功能按钮')
        plus_button.click()
        time.sleep(5)

        # 选择“发起群聊”并点击进入
        FQQL = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发起群聊")')
        FQQL.click()
        time.sleep(5)

        # 在搜索框输入
        seach = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索")')
        seach.send_keys("a")

        # 验证搜索结果
        search_results = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("a")')
        self.assertTrue(any('a' in result.text for result in search_results))

        print("测试用例WX-CSYL-0564通过:验证用户能通过搜索找到特定联系人")

if __name__ == '__main__':
    unittest.main()