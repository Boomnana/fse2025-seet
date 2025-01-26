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

# 点击【趣测】进入我的运势页面
fun_test_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="趣测"]')
fun_test_button.click()
time.sleep(5)

# 检查页面是否显示有恋爱运、学业/事业运、金钱运
fortune_types = ['恋爱运', '学业/事业运', '金钱运']
for fortune_type in fortune_types:
    if not driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{fortune_type}"]'):
        print(f"测试失败：页面未显示{fortune_type}")
        driver.quit()
        exit()

print("测试通过：页面显示所有分类运势")

# 结束测试，关闭Appium会话
driver.quit()