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

    # 点击笔记
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH,
                                    "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='笔记']"))
    )
    notes_button = driver.find_element(AppiumBy.XPATH,
                                       "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='笔记']")
    notes_button.click()

    # 对推荐进行点赞
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/trackLikeBtn"))
    )
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