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

# 点击云贝中心进入云贝中心页面
cloud_bee_center_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="云贝中心"]')
cloud_bee_center_button.click()
time.sleep(5)

# 获取云贝数量的显示元素
cloud_bee_amount = driver.find_element(AppiumBy.ID, 'com.netease.cloudmusic:id/tv_cloudbee_count')

# 假设我们知道云贝的正确数量，这里用expected_cloud_bee代替
expected_cloud_bee = '123456'  # 假设用户应该有的云贝数量

# 检查云贝数量是否准确显示
if cloud_bee_amount.text == expected_cloud_bee:
    print("测试通过：云贝数量正确显示")
else:
    print("测试失败：云贝数量显示不正确，预期为 {}".format(expected_cloud_bee))

# 结束测试，关闭Appium会话
driver.quit()