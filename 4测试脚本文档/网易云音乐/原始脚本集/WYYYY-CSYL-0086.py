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

# 等待网易云音乐启动并进入商城中心
time.sleep(5)
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="网易云音乐"]').click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="商城中心"]').click()
time.sleep(5)

# 点击右上方的购物车标识进入购物车管理页面
cart_icon = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@contentDescription="购物车"]')
cart_icon.click()
time.sleep(5)

# 在购物车页面选择一个商品，这里我们选择第一个商品
first_product = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.FrameLayout')[1]
checkbox = first_product.find_element(AppiumBy.XPATH, './/android.widget.CheckBox')
checkbox.click()
time.sleep(1)

# 点击管理按钮，显示删除按钮
management_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="管理"]')
management_button.click()
time.sleep(2)

# 点击删除按钮，弹出确认对话框
delete_button = first_product.find_element(AppiumBy.XPATH, './/android.widget.Button[@text="删除"]')
delete_button.click()
time.sleep(2)

# 确认删除操作
confirm_delete = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="删除"]')
confirm_delete.click()
time.sleep(2)

# 验证商品是否从购物车中移除
try:
    first_product.find_element(AppiumBy.XPATH, './/android.widget.TextView')
    print("测试失败：商品未从购物车中移除")
except Exception as e:
    print("测试通过：商品已从购物车中移除")

# 结束测试，关闭Appium会话
driver.quit()