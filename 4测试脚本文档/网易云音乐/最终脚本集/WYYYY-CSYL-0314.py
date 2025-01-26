from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# appium-python-client 2.10.0
# selenium 4.10
# appium 1.17.1
# 网易云音乐 9.1.60
options = UiAutomator2Options().load_capabilities({
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": ".activity.IconChangeDefaultAlias",
    #'noReset': True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
})

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
print('当前用例：通知栏样式')
size = driver.get_window_size()
# 获取屏幕宽度
width = size['width']

# 获取屏幕高度
height = size['height']

print(width)
print(height)
# app起始页（点同意）

try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/agree")
    # 定位
    element.click()
    # 对元素进行操作

except Exception as e:
    print("起始页发生错误：", e)

sleep(1)

# app起始页（点允许）
try:
    sleep(1)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击立即体验）
try:
    sleep(6)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/trialT")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击同意）
try:
    sleep(1)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/positiveBtn")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# 进入首页（点击允许）
try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# 首页-选项
try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/menu_icon")
    # 定位
    element.click()
    # 对元素进行操作

except Exception as e:
    print("首页-选项发生错误：", e)

# 首页-选项-滚动到设置并点击
try:
    sleep(5)
    # 等待元素加载完成
    # driver.tap([(340,739)])  # 原先元素的坐标

    x1 = int(width * 730 / 900)
    y1 = int(height * 1540 / 1600)
    x2 = int(width * 730 / 900)
    y2 = int(height * 416 / 1600)
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    # 滚动到设置
    x3 = int(width * 676 / 900)
    y3 = int(height * 585 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
    # 点击设置

except Exception as e:
    print("首页-选项-滚动到设置点击发生错误：", e)

# 首页-选项-设置-滚动-通知栏样式
try:
    sleep(3)
    # 等待元素加载完成
    x1 = int(width * 406 / 900)
    y1 = int(height * 168 / 1600)
    x2 = int(width * 403 / 900)
    y2 = int(height * 1534 / 1600)
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    # 滚动到通知栏样式
    # 等待并检查自动更新元素是否存在（根据文本内容）
    wait = WebDriverWait(driver, 2)
    lyric_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, '通知栏样式')]"))  # 替换为实际文本
    )
    sleep(1)
    # 点击打开
    lyric_element.click()
    if lyric_element.is_displayed():
        print("测试通过")
    else:
        print("测试不通过")

except Exception as e:
    print("首页-选项-设置-滚动到通知栏样式：", e)





driver.quit()
