from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
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

    # 点击“其他登录方式”
    other_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView")
    other_login_button.click()

    # 勾选“我已阅读并同意”
    agree_checkbox = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 点击微信登录
    wx_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/wx")
    wx_login_button.click()

    # 等待进入主页并点击“我的”
    time.sleep(5)  # 等待微信登录完成
    my_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='我的']")
    my_button.click()

    # 点击“本地”
    local_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/nameDragonBall' and @text='本地']")
    local_button.click()

    # 验证本地音乐列表是否按属性分类显示
    time.sleep(2)
    music_list = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text(), '未知')]")
    assert len(music_list) > 0, "本地音乐列表未显示"

finally:
    # 关闭webdriver
    driver.quit()