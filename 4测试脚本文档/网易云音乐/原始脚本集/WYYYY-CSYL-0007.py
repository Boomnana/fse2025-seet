from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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

    # 输入手机号
    phone_number = "159896666"
    phone_input = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/cellphone")
    phone_input.send_keys(phone_number)

    # 不勾选“我已阅读并同意”
    agree_checkbox = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()  # 如果已经勾选，则点击一次可以取消勾选

    # 点击“验证码登录”按钮
    login_button = driver.find_element(MobileBy.ID, "com.netease.cloudmusic:id/newLoginBtn")
    login_button.click()

    # 等待并验证是否弹出服务协议和隐私政策的提示
    time.sleep(2)
    popup = driver.find_element(MobileBy.XPATH, "//*[contains(text(), '服务协议和隐私政策等指引')]")
    assert popup is not None, "未弹出服务协议和隐私政策的提示"

finally:
    # 关闭webdriver
    driver.quit()