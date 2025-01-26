# 初始化Appium WebDriver
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


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
# 点击右上角工具栏图标
toolbar = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="抽屉菜单"]/android.widget.ImageView')
toolbar.click()
time.sleep(10)  # 等待菜单展开

# 点击【趣测】进入我的运势页面
fun_test_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="点击查看今日运势"]')
fun_test_button.click()
time.sleep(10)

# 进入运势中心，查看分类运势（恋爱运、学业/事业运、金钱运
# parent = driver.find_element(AppiumBy.CLASS_NAME,'android.view.View')
if driver.find_element_by_android_uiautomator("text('恋爱运')") and driver.find_element_by_android_uiautomator("text('学业/事业运')") and driver.find_element_by_android_uiautomator("text('金钱运')"):
    print("测试通过：分类运势信息准确")
else:
    print("测试失败:分类运势信息不准确")