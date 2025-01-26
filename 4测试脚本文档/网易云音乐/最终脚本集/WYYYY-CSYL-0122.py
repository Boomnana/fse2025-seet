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


# 点击云贝中心进入云贝中心页面
cloud_bee_center_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("云贝中心")')
cloud_bee_center_button.click()
time.sleep(5)

# 获取云贝数量的显示元素
cloud_bee_amount = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("0")')

# 假设我们知道云贝的正确数量，这里用expected_cloud_bee代替
expected_cloud_bee = '0'  # 假设用户应该有的云贝数量

# 检查云贝数量是否准确显示
if cloud_bee_amount.text == expected_cloud_bee:
    print("测试通过：云贝数量正确显示")
else:
    print("测试失败：云贝数量显示不正确，预期为 {}".format(expected_cloud_bee))

# 结束测试，关闭Appium会话
driver.quit()