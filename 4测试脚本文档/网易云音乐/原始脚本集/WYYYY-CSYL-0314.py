
#根据您的要求，以下是使用appium-python编写的自动化测试脚本，该脚本将执行网易云音乐应用中选择通知栏显示样式的功能测试。脚本中包含了WebDriverWait和expected_conditions来动态等待元素状态，以及TouchAction和UiAutomator2Options来提升脚本的效率和稳定性，并在关键操作处添加了try-catch结构。

# ```python
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
print('当前用例：选择网易云音乐通知栏显示样式')

# 获取屏幕大小
size = driver.get_window_size()
width = size['width']
height = size['height']

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

# 等待元素加载并点击同意
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/positiveBtn"))
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

# 点击通知栏样式
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.TextView[@text='通知栏样式']"))
    )
    element.click()
except Exception as e:
    print("点击通知栏样式发生错误：", e)

# 选择一个样式
try:
    # 假设样式列表是水平滑动的，且我们选择第一个样式
    x = int(width * 0.25)  # 根据实际比例调整
    y = int(height * 0.6)  # 根据实际比例调整
    TouchAction(driver).tap(x=x, y=y).perform()
except Exception as e:
    print("选择样式发生错误：", e)

# 验证通知栏样式是否已更改
try:
    # 这里需要根据实际的通知栏样式更改来编写验证逻辑
    # 例如，检查通知栏中网易云音乐的通知是否显示为所选样式
    pass
except Exception as e:
    print("验证通知栏样式发生错误：", e)

# 关闭WebDriver
driver.quit()
#```

#请注意，您需要根据网易云音乐应用的实际元素ID和文本内容来调整脚本中的元素定位器。此外，由于网易云音乐的版本更新可能会导致界面元素发生变化，因此您可能需要根据实际情况更新脚本中的元素定位逻辑。
