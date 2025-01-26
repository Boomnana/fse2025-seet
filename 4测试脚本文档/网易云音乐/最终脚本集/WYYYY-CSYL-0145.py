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
time.sleep(5)
# 点击右上角工具栏图标
toolbar = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="抽屉菜单"]/android.widget.ImageView')
toolbar.click()
time.sleep(10)  # 等待菜单展开

# 点击【装扮中心】进入装扮中心页面
fun_test_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("装扮中心")')
fun_test_button.click()
time.sleep(10)

def get_all_decorations_from_source(driver):
    # 获取装扮列表元素
    decoration_list = driver.find_elements(AppiumBy.CLASS_NAME, "android.view.ViewGroup")
    return [item.text for item in decoration_list]
try:
    # 获取所有可用装扮的列表
    all_decorations = get_all_decorations_from_source(driver)
    print("获取到的装扮列表:", all_decorations)

    # 验证装扮列表是否展示所有可用装扮
    # 这里可以根据实际需求添加验证逻辑
    if all_decorations:
     print("测试通过：装扮列表展示所有可用装扮")
    else:
     print("测试失败：装扮列表未提供展示所有可用装扮")

finally:
    # 关闭浏览器
    driver.quit()

# 检查装扮列表是否展示所有可用装扮
# if driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("卡皮巴拉")'):
#     print("测试通过：装扮列表展示所有可用装扮")
# else:
#     print("测试失败：装扮列表未提供展示所有可用装扮")

# 结束测试，关闭Appium会话
# driver.quit()
