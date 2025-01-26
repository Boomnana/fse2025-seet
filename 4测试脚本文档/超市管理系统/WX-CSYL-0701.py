import os
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.common.actions import interaction
from appium.webdriver.extensions.action_helpers import ActionHelpers
from appium.options.android import UiAutomator2Options

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',
                           options=UiAutomator2Options().load_capabilities(desired_caps))

driver.implicitly_wait(10)

# 等待发现按钮可见并点击
time.sleep(8)
discoverButton = driver.find_elements(By.ID, 'com.tencent.mm:id/h6y')[2].click()

# 等待视频号标题可见并点击
time.sleep(8)
video = driver.find_elements(By.ID,'android:id/title')[1].click()

#滑动视频，设置了一个可控循环，选y为执行操作，选n为退出该循环
while True:
    user_input = input("是否下滑到下一个视频？(y/n): ")
    if user_input.lower() == 'y':
        print("执行操作")
        time.sleep(10)  # 等待10秒
        driver.swipe(542, 1422, 540, 810)  # 执行滑动操作
    elif user_input.lower() == 'n':
        print("退出程序")
        break
    else:
        print("输入无效，请输入 'y' 或 'n'")

screenshot_dir = 'C:\\Users\\17586\\Desktop\\lzycode\\截屏'  # 替换为您想要保存截图的目录
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)  # 如果目录不存在，则创建它
# timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_filename = f"WX-CSYL-0701.py.png"
screenshot_path = os.path.join(screenshot_dir, screenshot_filename)