from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

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

# 点击性别
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/ecb")
  element.click()
except Exception as e:
  print("点击性别发生错误：", e)

sleep(2)

# 选择性别
try:
    element = driver.find_element(By.ID, "com.ss.android.article.news:id/ftb")
    element2 = driver.find_element(By.ID, "com.ss.android.article.news:id/cv")
    # 获取控件的bounds
    bounds = element.location
    width = element.size['width']
    height = element.size['height']
    print(width)
    print(height)
    # 计算x轴中间位置
    middle_x = bounds['x'] + (width // 2)
    # 计算y轴偏下三分之一的位置
    one_third_down_y = bounds['y'] + (height // 3) * 2 + 30
    sleep(1)
    TouchAction(driver).tap(x=middle_x, y=one_third_down_y).perform()
    sleep(1)
    # 获取控件的文本
    msg = element.text
    sleep(1)
    print(f"已点击屏幕上的坐标：({middle_x}, {one_third_down_y})")
    print(msg)
    element2.click()
    sleep(1)
    element3 = driver.find_element(By.ID, "com.ss.android.article.news:id/imh")
    test = element3.text
    assert test in msg, f"选择的性别：{msg}与显示的性别：{test}不一致"
    print("测试通过，选择的性别已被保存")
except Exception as e:
    print("发生错误：", e)

finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()
