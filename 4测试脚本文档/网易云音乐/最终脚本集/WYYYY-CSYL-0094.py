# 初始化Appium WebDriver
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "7b2ec43e",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": "com.netease.cloudmusic.activity.MainActivity",
    "resetKeyboard": True,
    "noReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 进入消息模块
def enter_message():
    time.sleep(2)  # 等待页面加载
    # 点击右下角的【我的】按钮
    my_button = driver.find_element(AppiumBy.ID, 'com.netease.cloudmusic:id/icon')
    my_button.click()
    time.sleep(2)
    # 点击右上角工具栏图标
    toolbar = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="抽屉菜单"]/android.widget.ImageView')
    toolbar.click()
    time.sleep(3)  # 等待菜单展开
    # 点击“我的消息”
    message = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的消息")')
    message.click()
    time.sleep(2)  # 等待消息页面加载

# 验证消息列表是否完整展示
def verify_message_list():
    message_list = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[1]  # 消息列表的ID
    if message_list.is_displayed():
        print("消息列表完整展示，测试通过")
    else:
        print("消息列表未完整展示，测试失败")

# 主流程
def main():
    enter_message()
    verify_message_list()
    driver.quit()

if __name__ == '__main__':
    main()