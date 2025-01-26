import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

class WeChatRegistrationTest(unittest.TestCase):
    def setUp(self):
        # 初始化Appium WebDriver
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
        time.sleep(20)

    def tearDown(self):
        # 关闭WebDriver
        self.driver.quit()
    """测试用例WX-CSYL-0633:验证密码强度和格式要求。"""
    def test_registration_with_weak_password(self):
        # 点击注册按钮
        register_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("注册")')
        register_button.click()
        time.sleep(5)

        # 填写有效手机号
        phone_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请填写手机号")')
        phone_input.send_keys('12345678901')

        # 填写用户名
        username_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("例如：陈晨")')
        username_input.send_keys('test_user')
        # 填写弱密码
        password_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("填写密码")')
        password_input.send_keys('weak')

        # 同意协议
        agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '同意')
        agree.click()

        # 点击注册按钮
        submit_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("同意并继续")')
        submit_button.click()
        time.sleep(5)

        # 验证是否显示密码强度不足的错误提示
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("注册失败")'))
        )
        print("测试用例WX-CSYL-0633通过：有密码强度要求。")

if __name__ == '__main__':
    unittest.main()