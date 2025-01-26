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

print('输入朋友圈文字内容')
thought = input('这一刻的想法...')



# 等待发现按钮可见并点击
time.sleep(8)
discoverButton = driver.find_elements(By.ID, 'com.tencent.mm:id/h6y')[2].click()

# 等待朋友圈标题可见并点击
time.sleep(8)
friend = driver.find_elements(By.ID,'android:id/title')[0].click()

# 等待朋友圈右上角的“拍摄”按钮可见
time.sleep(8)
friendPublish = driver.find_element(By.ID, 'com.tencent.mm:id/coz')

#在这段代码中，我们首先通过ActionChains对象的move_to_element方法移动到目标元素，然后使用click_and_hold模拟按下动作,
#pause方法用于指定按住的时间，最后通过release方法模拟释放动作，并调用perform方法执行整个动作链。
#请注意，长按的时间是通过pause方法的参数来设置的，单位是秒。如果你需要更精确的控制，可以适当调整这个值。
actions = ActionChains(driver)
actions.move_to_element(friendPublish).click_and_hold().pause(3).release().perform()

time.sleep(8)

#若出现提示“该功能为内部体验界面”，点击“我知道了”
iknow = driver.find_elements(By.ID, "com.tencent.mm:id/hrn")
if iknow:
    iknow.click()

#输入朋友圈中“这一刻的想法”
textPublish = driver.find_element(By.ID, 'com.tencent.mm:id/n7y').send_keys(thought)
time.sleep(8)
#点击“发表”
publish = driver.find_element(By.ID, 'com.tencent.mm:id/fp').click()
time.sleep(8)

screenshot_dir = 'C:\\Users\\17586\\Desktop\\lzycode\\截屏'  # 替换为您想要保存截图的目录
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)  # 如果目录不存在，则创建它
# timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_filename = f"WX-CSYL-0650.py.png"
screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

# 截取当前界面的屏幕截图，并保存到指定路径
driver.save_screenshot(screenshot_path)
print(f'Screenshot saved to {screenshot_path}')

# 其他操作...

# 关闭会话
driver.quit()