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


    #系统权限弹窗
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]"))
    )
    always_agree_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]")
    always_agree_button.click()


    # 等待进入主页并点击“我的”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='我的']"))
    )
    my_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/desc' and @text='我的']")
    my_button.click()

    # 点击“本地”
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/nameDragonBall' and @text=\"本地\"]"))
    )
    local_button = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.netease.cloudmusic:id/nameDragonBall' and @text=\"本地\"]")
    local_button.click()

    # 系统权限弹窗
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='始终允许]"))
    )
    always_agree_button2 = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='始终允许]")
    always_agree_button2.click()

    # 立即扫描
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@resource-id=’com.netease.cloudmusic:id/localmusicScanBtn‘ and @text=\"立即扫描\"]"))
    )
    scan_button = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id=’com.netease.cloudmusic:id/localmusicScanBtn‘ and @text=\"立即扫描\"]")
    scan_button.click()

    # 使用此文件
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
    )
    use_button = driver.find_element(AppiumBy.ID,"android:id/button1")
    use_button.click()

    # 使用此文件
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
    )
    use_agree_button = driver.find_element(AppiumBy.ID, "android:id/button1")
    use_agree_button.click()

    # 等待并验证错误提示是否出现
    WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text(), '未知')]"))
    )
    music_list = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text(), '未知')]")
    assert len(music_list) > 0, "本地音乐列表未显示"

finally:
    # 关闭webdriver
    driver.quit()