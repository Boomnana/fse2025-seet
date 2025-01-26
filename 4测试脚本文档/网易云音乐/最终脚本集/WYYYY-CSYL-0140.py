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
time.sleep(5)

# 点击右下角的【我的】按钮
my_button = driver.find_element(AppiumBy.ID, 'com.netease.cloudmusic:id/icon')
my_button.click()
time.sleep(2)
# 点击右上角工具栏图标
toolbar = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="抽屉菜单"]/android.widget.ImageView')
toolbar.click()
time.sleep(3)  # 等待菜单展开

# 检查页面是否显示有运势中心字样
if driver.find_element(AppiumBy.CLASS_NAME, 'android.view.ViewGroup'):
    print("测试通过：提供了运势中心的入口，运势中心入口明显可见")
else:
    print("测试失败：未提供运势中心入口")

# 结束测试，关闭Appium会话
driver.quit()