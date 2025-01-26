from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

# 设置Appium服务器地址和端口
appium_server = 'http://localhost:4723/wd/hub'

# 设置desired capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'your_device_name',
    'appPackage': 'com.netease.cloudmusic',
    'appActivity': 'com.netease.cloudmusic.activity.WelcomeActivity',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

# 初始化webdriver
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 等待元素加载
    time.sleep(2)

    # 输入格式错误的手机号
    incorrect_phone_number = "12345"
    phone_input = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/cellphone")
    phone_input.send_keys(incorrect_phone_number)

    # 勾选“我已阅读并同意”
    agree_checkbox = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 点击“验证码登录”按钮
    login_button = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/newLoginBtn")
    login_button.click()

    # 等待并验证错误提示是否出现
    time.sleep(2)
    error_message = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/error_message").text
    assert "请输入11位数字的手机号" in error_message, "手机号格式错误提示未出现"

finally:
    # 关闭webdriver
    driver.quit()