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

    # 点击左上角侧边栏图标
    sidebar_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/trackLikeBtn")  # 注意：这里的ID可能需要根据实际情况调整
    sidebar_button.click()

    # 点击“音乐黑名单”
    blacklist_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='音乐黑名单']")
    blacklist_button.click()

    # 验证黑名单中的歌手、单曲和分类列表是否正确展示
    time.sleep(2)
    blacklist_items = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text(), '歌手') or contains(@text(), '单曲') or contains(@text(), '分类')]")
    assert len(blacklist_items) > 0, "黑名单中的歌手、单曲和分类列表未正确展示"

finally:
    # 关闭webdriver
    driver.quit()