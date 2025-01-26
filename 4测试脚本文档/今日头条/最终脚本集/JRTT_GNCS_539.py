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

sleep(1)

# 点击编辑资料
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/ec2")
  element.click()
except Exception as e:
  print("点击编辑资料发生错误：", e)

sleep(1)

# 点击职业
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/edb")
  element.click()
except Exception as e:
  print("点击职业发生错误：", e)

sleep(2)

# 选择职业
try:
    element = driver.find_element(By.ID, "com.ss.android.article.news:id/cfi")
    element1 = driver.find_element(By.ID, "com.ss.android.article.news:id/gef")
    element2 = driver.find_element(By.ID, "com.ss.android.article.news:id/a2q")

    bounds = element.location
    width = element.size['width']
    height = element.size['height']

    x1 = width * 0.25
    x2 = width * 0.74
    y = bounds['y'] + height * 0.66
    print(x1)
    print(x2)
    print(y)

    sleep(1)
    TouchAction(driver).tap(x=x1, y=y).perform()
    sleep(1)
    TouchAction(driver).tap(x=x2, y=y).perform()
    sleep(1)

    string = element2.text

    element4 = driver.find_element(By.ID, "com.ss.android.article.news:id/cv")
    element4.click()
    sleep(1)

    element5 = driver.find_element(By.ID, "com.ss.android.article.news:id/izz")
    data = element5.text

    assert data in string, f"选择的职业：{string}与显示的职业：{data}不一致"
    print("测试通过，选择的职业已被正确显示")
except Exception as e:
    print("选择职业发生错误：", e)

finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()