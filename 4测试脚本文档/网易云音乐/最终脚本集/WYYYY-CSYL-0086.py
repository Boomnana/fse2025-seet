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
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#点击同意
management_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("同意")')
management_button.click()
time.sleep(2)

#点击始终允许
management_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("始终允许")')
management_button.click()
time.sleep(2)

#点击同意协议
management_button = driver.find_element(AppiumBy.ID,"com.netease.cloudmusic:id/agreeCheckbox")
management_button.click()
time.sleep(2)

#点击一键登录
management_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("一键登录")')
management_button.click()
time.sleep(2)

# 点击右下角的【我的】按钮
my_button = driver.find_element(AppiumBy.ID, 'com.netease.cloudmusic:id/icon')
my_button.click()
time.sleep(2)
# 点击右上角工具栏图标
toolbar = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="抽屉菜单"]/android.widget.ImageView')
toolbar.click()
time.sleep(3)  # 等待菜单展开

# 点击商城中心
driver.find_element(AppiumBy.ID, 'com.netease.cloudmusic:id/container').click()

# 等待进入商城中心页面
time.sleep(2)

# 点击右上方的购物车标识进入购物车管理页面
cart_icon = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Image')[0]
cart_icon.click()
time.sleep(5)

# 点击管理按钮，显示删除按钮
management_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("管理")')
management_button.click()
time.sleep(2)

# 在购物车页面选择一个商品，这里我们选择第一个商品
first_product = driver.find_elements(AppiumBy.XPATH, '//android.view.View[@resource-id="cart"]/android.view.View[4]/android.view.View')
first_product.click()
time.sleep(1)

# 点击删除按钮，弹出确认对话框
delete_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("删除")')
delete_button.click()
time.sleep(2)

# 确认删除操作
confirm_delete = driver.find_element(AppiumBy.XPATH, '//android.view.View[@text="删除"])[2]')
confirm_delete.click()
time.sleep(2)

# 验证商品是否从购物车中移除
try:
    first_product.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="cart"]/android.view.View[4]/android.view.View')
    print("测试失败：商品未从购物车中移除")
except Exception as e:
    print("测试通过：商品已从购物车中移除")

# 结束测试，关闭Appium会话
driver.quit()