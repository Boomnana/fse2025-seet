from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# 初始化Appium WebDriver
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.0',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.netease.cloudmusic',
    'appActivity': 'com.netease.cloudmusic.activity.SplashActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待网易云音乐启动并登录
time.sleep(5)

# 点击左上角的工具栏标识
menu_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="网易云音乐"]')
menu_button.click()
time.sleep(2)

# 点击【云村有票】进入我的运势页面
fun_test_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="云村有票"]')
fun_test_button.click()
time.sleep(5)

# 查看热门演出列表
if driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="热门演出"]'):
    print("测试通过：热门演出列表展示最新演出")
else:
    print("测试失败：热门演出未展示")

# 结束测试，关闭Appium会话
driver.quit()