# 初始化Appium WebDriver
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "127.0.0.1:5554 ",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": "com.netease.cloudmusic.activity.MainActivity",
    "resetKeyboard": True,
    "noReset": True
})
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

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

# 点击【云村有票】进入云村有票页面
fun_test_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("云村有票")')
fun_test_button.click()
time.sleep(10)

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().CLASS_NAME("android.view.View").childSelector(new UiSelector().text("Livehouse"))'):
# 查看热门演出列表
# parent = driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="full-scroll-container"]/android.view.View[2]')
if driver.find_element_by_android_uiautomator("text('热门演出')"):
    print("测试通过：热门演出列表展示最新演出")
else:
    print("测试失败：热门演出未展示")

# 结束测试，关闭Appium会话
driver.quit()


