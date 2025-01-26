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

    # 等待微信登录完成
    time.sleep(10)

    # 点击笔记
    notes_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='笔记']")
    notes_button.click()

    # 对推荐进行点赞
    like_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/trackLikeBtn")
    like_count_before = int(like_button.get_attribute('text').replace(' ', ''))
    like_button.click()
    time.sleep(2)
    like_count_after = int(like_button.get_attribute('text').replace(' ', ''))

    # 验证点赞数是否增加
    assert like_count_after == like_count_before + 1, "点赞数未增加"

finally:
    # 关闭webdriver
    driver.quit()