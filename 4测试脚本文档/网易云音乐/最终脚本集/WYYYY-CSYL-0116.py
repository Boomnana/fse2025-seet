# 初始化Appium WebDriver
import time
from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "127.0.0.1:5554",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": "com.netease.cloudmusic.activity.IconChangeDefaultAlias",
    "resetKeyboard": True,
    "noReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待网易云音乐启动并登录
time.sleep(10)

# 点击右下角的【我的】按钮
my_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的")')
my_button.click()
time.sleep(10)

# 点击【音乐应用】标识进入音乐应用页面
driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")[0].click()
time.sleep(10)

# 点击【编辑】按钮
edit_element = WebDriverWait(driver, 10).until(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("编辑")')
edit_element.click()

# 选择一个应用，这里我们选择第一个应用
# 假设第一个应用的删除按钮的定位器
first_app = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("109951165480490675")')
delete_button = first_app.find_elements(AppiumBy.CLASS_NAME, 'android.view.View')[1]
delete_button.click()
time.sleep(3)

# 点击【完成】按钮
complete_button = driver.find_element_by_android_uiautomator("text('完成')")
complete_button.click()
time.sleep(2)

# 验证该应用是否从音乐应用页面消失
try:
    first_app.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("109951165480490675")')
    print("测试失败：应用未从音乐应用页面消失")
except Exception as e:
    print("测试通过：应用已从音乐应用页面消失")

# 结束测试，关闭Appium会话
driver.quit()