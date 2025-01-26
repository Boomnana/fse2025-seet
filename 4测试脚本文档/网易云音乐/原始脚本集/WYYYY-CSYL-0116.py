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

# 点击右下角的【我的】按钮
my_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="我的"]')
my_button.click()
time.sleep(2)

# 点击【音乐应用】标识进入音乐应用页面
music_apps_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="音乐应用"]')
music_apps_button.click()
time.sleep(5)

# 点击【编辑】按钮
edit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="编辑"]')
edit_button.click()
time.sleep(2)

# 选择一个应用，这里我们选择第一个应用
# 假设第一个应用的删除按钮的定位器
first_app = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.FrameLayout')[0]
delete_button = first_app.find_element(AppiumBy.XPATH, './/android.widget.ImageButton')
delete_button.click()
time.sleep(1)

# 点击【完成】按钮
complete_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="完成"]')
complete_button.click()
time.sleep(2)

# 验证该应用是否从音乐应用页面消失
try:
    first_app.find_element(AppiumBy.XPATH, './/android.widget.TextView')
    print("测试失败：应用未从音乐应用页面消失")
except Exception as e:
    print("测试通过：应用已从音乐应用页面消失")

# 结束测试，关闭Appium会话
driver.quit()