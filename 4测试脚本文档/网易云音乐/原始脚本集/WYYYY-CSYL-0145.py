from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

from appium.webdriver.common.mobileby import MobileBy

# 初始化Appium WebDriver
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.0',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.netease.cloudmusic',
    'appActivity': 'com.netease.cloudmusic.activity.SplashActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待网易云音乐启动并登录
time.sleep(5)

# 点击左上角的工具栏标识
menu_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="网易云音乐"]')
menu_button.click()
time.sleep(2)

# 点击【装扮中心】进入装扮中心页面
fun_test_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='装扮中心']")
fun_test_button.click()
time.sleep(5)

def get_all_decorations_from_source(driver):
    # 获取装扮列表元素
    decoration_list = driver.find_elements(MobileBy.XPATH, "//android.widget.TextView[contains(@text, '装扮')]")
    return [item.text for item in decoration_list]

# 初始化WebDriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    # 获取所有可用装扮的列表
    all_decorations = get_all_decorations_from_source(driver)
    print("获取到的装扮列表:", all_decorations)

    # 验证装扮列表是否展示所有可用装扮
    # 这里可以根据实际需求添加验证逻辑

finally:
    # 关闭浏览器
    driver.quit()