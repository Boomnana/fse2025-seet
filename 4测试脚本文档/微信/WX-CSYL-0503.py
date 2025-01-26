import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

class WeChatLoginOptionsTest(unittest.TestCase):
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
        # Initialize the Appium driver
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        time.sleep(40)

    def tearDown(self):
        # 关闭WebDriver
        self.driver.quit()

    """测试用例WX-CSYL-0503:验证“找回密码”和“紧急冻结”选项是否可用"""
    def test_login_options(self):
        # 点击登录
        login= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')
        login.click()
        time.sleep(2)

        # 点击“用微信号/QQ号/邮箱登录”
        login = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("用微信号/QQ号/邮箱登录")')
        login.click()
        time.sleep(5)

        # 点击“找回密码”选项
        sec = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("找回密码")')
        sec.click()
        time.sleep(5)

        # 返回登录页面
        self.driver.back()

        # 点击“紧急冻结”选项
        eme = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紧急冻结")')
        eme.click()
        time.sleep(5)

        print("测试用例WX-CSYL-0503通过：“找回密码”和“紧急冻结”选项可用。")


if __name__ == '__main__':
    unittest.main()