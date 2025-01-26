from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Appium服务器地址和端口
appium_server = 'http://localhost:4723/wd/hub'

desired_caps = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "jbfex8prdqcuxgmr",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": "com.netease.cloudmusic.activity.MainActivity",
    "appium:unicodeKeyboard": "true",
    "appium:resetKeyboard": "true"
}

# 初始化webdriver
options = UiAutomator2Options().load_capabilities(desired_caps)

# 初始化 Appium 驱动
driver = webdriver.Remote(appium_server, options=options)

try:
    # 等待并同意用户条款进入登录页
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/agree"))
    )
    agree_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agree")
    agree_button.click()

    # 点击“其他登录方式”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView"))
    )
    other_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView")
    other_login_button.click()

    # 等待并勾选“我已阅读并同意”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox"))
    )
    agree_checkbox = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 点击微信登录
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/wx"))
    )
    wx_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/wx")
    wx_login_button.click()

    # 系统权限弹窗
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]"))
    )
    always_agree_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]")
    always_agree_button.click()

    # 点击左上角侧边栏图标
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.netease.cloudmusic:id/trackLikeBtn"))
    )
    sidebar_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/trackLikeBtn")  # 注意：这里的ID可能需要根据实际情况调整
    sidebar_button.click()

    # 点击“音乐黑名单”
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='音乐黑名单']"))
    )
    blacklist_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='音乐黑名单']")
    blacklist_button.click()

    # 验证黑名单中的歌手、单曲和分类列表是否正确展示
    time.sleep(2)
    blacklist_items = driver.find_elements(AppiumBy.XPATH,
                                           "//android.widget.TextView[contains(@text(), '歌手') or contains(@text(), '单曲') or contains(@text(), '分类')]")
    assert len(blacklist_items) > 0, "黑名单中的歌手、单曲和分类列表未正确展示"

finally:
    # 关闭webdriver
    driver.quit()