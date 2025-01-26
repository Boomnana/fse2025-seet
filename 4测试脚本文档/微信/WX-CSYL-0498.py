import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

class WeChatLanguageSettingTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:5554',  # 确保这是你的设备或模拟器的正确地址
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            # com.tencent.mm.plugin.account.ui.WelcomeActivity
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            # 可能还需要添加其他配置，如自动化名称、新命令超时等
        }

        options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        time.sleep(10)

    def tearDown(self):
        # 关闭WebDriver
        self.driver.quit()

    """测试用例WX-CSYL-0498:验证语言设置选项是否有效"""
    def test_language_setting(self):

        # 点击语言设置选项
        language_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("语言")')
        language_button.click()
        time.sleep(5)

        # 选择英语
        english_language = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("English")')
        english_language.click()
        time.sleep(2)

        # 点击保存按钮
        save_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("保存")')
        save_button.click()
        time.sleep(5)

        # 验证是否修改成功
        lag = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("English")')
        res = lag.text
        self.assertEqual('English',res)
        time.sleep(5)

        print("测试用例WX-CSYL-0498通过：系统语言已更改为英语。")

if __name__ == '__main__':
    unittest.main()