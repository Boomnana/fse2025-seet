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

    #删除原有手机号
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/deleteBtn"))
    )
    delete_click = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/deleteBtn")
    delete_click.click()

    # 等待并输入格式错误的手机号
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/cellphone"))
     )
    phone_input = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/cellphone")
    phone_input.send_keys("15989651520")

    # 等待并点击“验证码登录”按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/newLoginBtn"))
    )
    login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/newLoginBtn")
    login_button.click()

    # 等待服务协议和隐私政策的提示出现
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ID, "com.netease.cloudmusic:id/title"))
    )
    popup = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/title")
    assert popup is not None, "未弹出服务协议和隐私政策的提示"

    # 等待并点击“不同意”按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/negativeBtn"))
    )
    disagree_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/negativeBtn")
    disagree_button.click()

    # 验证是否返回到登录页面
    time.sleep(2)
    login_page = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/cellphone")
    assert login_page is not None, "未返回到登录页面"

finally:
    # 关闭webdriver
    driver.quit()