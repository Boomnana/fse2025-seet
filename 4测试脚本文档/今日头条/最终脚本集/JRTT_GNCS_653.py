from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import re

desired_caps = {
  "platformName": "Android",
  "platformVersion": "12",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.ss.android.article.news",
  "appActivity": "com.ss.android.article.news.activity.MainActivity",
  "unicodeKeyboard": True,
  "resetKeyboard": True,
}

# app起始页（点同意）
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
try:
  sleep(10)
  # 等待元素加载完成
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/fs4")
  # 对元素进行操作，例如点击
  element.click()
  # 对元素进行操作，例如点击

except Exception as e:
  print("app起始页发生错误：", e)

sleep(2)

# 点击“我的”
try:
  element = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[6]/android.widget.TabWidget/com.bytedance.platform.raster.viewpool.cache.compat.MeasureOnceRelativeLayout2[4]")
  element.click()
except Exception as e:
  print("点击“我的”发生错误：", e)

sleep(2)

# 点击其他方式登录
try:
  element = driver.find_element(By.ID,"com.ss.android.article.news:id/fuo")
  element.click()
except Exception as e:
  print("点击其他方式登录发生错误：", e)

sleep(1)

# 点击密码登录
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/dpv")
  element.click()
except Exception as e:
  print("点击密码登录发生错误：", e)

sleep(1)

# 点击同意协议勾选框
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/g7p")
  element.click()
except Exception as e:
  print("点击同意协议勾选框发生错误：", e)

sleep(1)

# 输入手机号
try:
  input_element = driver.find_element(By.ID, "com.ss.android.article.news:id/ib")
  # 清除输入框中已有的内容（如果有）
  input_element.clear()
  # 在输入框中输入文本“123”
  input_element.send_keys("13532011556")
except Exception as e:
  print("输入手机号发生错误：", e)

sleep(1)

# 输入密码
try:
  input_element = driver.find_element(By.ID, "com.ss.android.article.news:id/ik")
  # 清除输入框中已有的内容（如果有）
  input_element.clear()
  # 在输入框中输入文本“123”
  input_element.send_keys("x1085245086y")
except Exception as e:
  print("输入密码发生错误：", e)

sleep(1)

# 点击登录
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/auz")
  element.click()
except Exception as e:
  print("点击登录发生错误：", e)

sleep(3)

# 关闭提示
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/bis")
  element.click()
except Exception as e:
  print("关闭提示发生错误：", e)

sleep(3)

# 点击设置
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/fcl")
  element.click()
except Exception as e:
  print("点击设置发生错误：", e)

sleep(2)

# 下滑
try:
  element1 = driver.find_element(By.ID, "com.ss.android.article.news:id/add")
  bounds1 = element1.location
  width1 = element1.size['width']
  height1 = element1.size['height']

  y1 = bounds1['y'] + height1

  element2 = driver.find_element(By.ID, "com.ss.android.article.news:id/h2k")
  bounds2 = element2.location
  width2 = element2.size['width']
  height2 = element2.size['height']

  y2 = bounds2['y']

  y3 = y1 + (y2-y1)/2

  element4 = driver.find_element(By.ID, "com.ss.android.article.news:id/hfu")
  bounds4 = element4.location
  width4 = element4.size['width']
  height4 = element4.size['height']

  y4 = bounds4['y'] + height4

  element5 = driver.find_element(By.ID, "com.ss.android.article.news:id/gl8")
  bounds5 = element5.location
  width5 = element5.size['width']
  height5 = element5.size['height']

  y5 = bounds5['y']

  y6 = y4 + (y5 - y4) / 2

  print(y3)
  print(y6)

  TouchAction(driver).press(x=500, y=y3).move_to(x=505, y=y6).release().perform()
except Exception as e:
  print("下滑：", e)

sleep(2)
# 点击退出
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/ect")
  element.click()
except Exception as e:
  print("点击退出发生错误：", e)

sleep(2)

# 点击确认
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/if")
  element.click()
except Exception as e:
  print("点击退出发生错误：", e)

sleep(2)
# 验证
try:
    # 使用id定位元素
    element = driver.find_element(By.ID, "com.ss.android.article.news:id/brf")
    print("测试通过，退出登录成功执行")
except Exception as e:
    print("测试失败，退出操作未执行", e)

finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()