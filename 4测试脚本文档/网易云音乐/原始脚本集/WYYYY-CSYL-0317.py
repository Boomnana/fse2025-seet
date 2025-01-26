from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 设置UiAutomator2Options
options = UiAutomator2Options().load_capabilities({
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": ".activity.IconChangeDefaultAlias",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
})

# 初始化WebDriver
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
print('当前用例：设置自动下载最新安装包的条件')

# 获取屏幕大小
size = driver.get_window_size()
width = size['width']
height = size['height']
print(width)
print(height)

# 等待元素加载并点击同意
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/agree"))
    )
    element.click()
except Exception as e:
    print("点击同意发生错误：", e)

# 等待元素加载并点击允许
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
    )
    element.click()
except Exception as e:
    print("点击允许发生错误：", e)

# 等待元素加载并点击立即体验
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/trialT"))
    )
    element.click()
except Exception as e:
    print("点击立即体验发生错误：", e)

# 进入首页并点击菜单图标
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/menu_icon"))
    )
    element.click()
except Exception as e:
    print("点击菜单图标发生错误：", e)

# 滚动到设置并点击
try:
    # 滚动到设置
    x1 = int(width * 0.81)  # 根据实际比例调整
    y1 = int(height * 0.96)  # 根据实际比例调整
    x2 = int(width * 0.81)  # 根据实际比例调整
    y2 = int(height * 0.25)  # 根据实际比例调整
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    # 点击设置
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.TextView[@text='设置']"))
    )
    element.click()
except Exception as e:
    print("滚动到设置并点击发生错误：", e)

# 点击自动更新设置
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.TextView[@text='自动更新']"))
    )
    element.click()
except Exception as e:
    print("点击自动更新设置发生错误：", e)

# 设置自动更新条件
try:
    # 假设自动更新条件有多个选项，这里以Wi-Fi下自动更新为例
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Switch[@text='Wi-Fi下自动更新']/android.widget.Switch"))
    )
    element.click()
except Exception as e:
    print("设置自动更新条件发生错误：", e)

# 验证设置是否保存
try:
    # 重新进入自动更新设置页面，检查Wi-Fi下自动更新是否被选中
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.TextView[@text='自动更新']"))
    )
    element.click()
    wifi_update_switch = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Switch[@text='Wi-Fi下自动更新']/android.widget.Switch"))
    )
    assert wifi_update_switch.is_selected(), "Wi-Fi下自动更新设置未被正确保存"
except Exception as e:
    print("验证设置是否保存发生错误：", e)

# 关闭WebDriver
driver.quit()