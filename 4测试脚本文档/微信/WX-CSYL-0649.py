import os
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.tencent.mm', # 启动APP Package名称
  'appActivity': 'com.tencent.mm.ui.LauncherUI', # 启动Activity名称
  'unicodeKeyboard': True, # 自动化需要输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',
  options=UiAutomator2Options().load_capabilities(desired_caps))

time.sleep(8)
def publish_moment_and_screenshot(driver, thought, screenshot_dir):
  driver.implicitly_wait(10)

  # 点击“发现”按钮
  discoverButton = driver.find_elements(By.ID, 'com.tencent.mm:id/h6y')[2]
  discoverButton.click()
  time.sleep(8)

  # 点击“发现”界面当中的“朋友圈”
  friend = driver.find_elements(By.ID, 'android:id/title')[0].click()
  time.sleep(8)

  # 点击朋友圈右上角的“拍摄”按钮
  friendPublish = driver.find_element(By.ID, 'com.tencent.mm:id/coz').click()
  time.sleep(8)

  # 点击“从相册选择”
  phoneFilm = driver.find_elements(By.ID, 'com.tencent.mm:id/gub')[1].click()
  time.sleep(10)

  # 选择第一张图片
  phoneSelect = driver.find_elements(By.ID, 'com.tencent.mm:id/jdh')[0].click()
  time.sleep(8)

  # 点击“完成”
  phoneFinish = driver.find_element(By.ID, 'com.tencent.mm:id/kaq').click()
  time.sleep(8)

  # 输入朋友圈中“这一刻的想法”
  textPublish = driver.find_element(By.ID, 'com.tencent.mm:id/n7y')
  textPublish.send_keys(thought)
  time.sleep(8)

  # 点击“发表”
  publish = driver.find_element(By.ID, 'com.tencent.mm:id/fp').click()
  time.sleep(8)

  # 保存截图
  if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)  # 如果目录不存在，则创建它
  # timestamp = time.strftime("%Y%m%d-%H%M%S")
  screenshot_filename = f"WX-CSYL-0649.py.png"
  screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
  driver.save_screenshot(screenshot_path)
  print(f"Screenshot saved to {screenshot_path}")


# 主函数
def main():
    print('输入朋友圈文字内容')
    thought = input('这一刻的想法...')
    screenshot_dir = 'C:\\Users\\17586\\Desktop\\lzycode\\截屏'  # 替换为您想要保存截图的目录
    publish_moment_and_screenshot(driver, thought, screenshot_dir)
    driver.quit()

