from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
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
    phone_input.send_keys("159896666")

    # 等待并勾选“我已阅读并同意”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox"))
    )
    agree_checkbox = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 等待并点击“验证码登录”按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/newLoginBtn"))
    )
    login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/newLoginBtn")
    login_button.click()

    #验证错误提示是否出现
    error_message = driver.find_element(AppiumBy.XPATH, "//android.widget.Toast[@text='请输入11位数字的手机号']").text
    assert "请输入11位数字的手机号" in error_message, "手机号格式错误提示未出现"
    

finally:
    # 关闭webdriver
    driver.quit()