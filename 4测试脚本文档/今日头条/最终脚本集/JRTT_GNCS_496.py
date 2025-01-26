from time import sleep
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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

sleep(1)

# 点击“我的”
try:
  element = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[6]/android.widget.TabWidget/com.bytedance.platform.raster.viewpool.cache.compat.MeasureOnceRelativeLayout2[4]")
  element.click()
except Exception as e:
  print("点击“我的”发生错误：", e)

sleep(1)

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

# 点击简介
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/eem")
  element.click()
except Exception as e:
  print("点击简介发生错误：", e)

sleep(2)

# 简介输入框
try:
    # 使用find_element方法和By类来定位输入框
    input_element = driver.find_element(By.ID, "com.ss.android.article.news:id/ewh")
    # 清除输入框中已有的内容（如果有）
    input_element.clear()
    # 尝试输入超过70个字符
    too_long_text = "1234563456789012345678903456789012345678903456789012345678903501234567890345678901234563456789012345678903456789012345678903456789012345678903456789012345678904567890123456789034567890123456789078901234567890ab"
    try:
        input_element.send_keys(too_long_text)
        print("输入框中已输入文本：", too_long_text)
    except WebDriverException as e:
        # 捕获错误信息并检查是否为期望的错误
        if "Cannot set the element to" in e.msg:
            print("简介输入框测试通过：捕获到期望的错误信息")
        else:
            print("简介输入框测试失败：", e)
except Exception as e:
    print("简介输入框发生错误：", e)


finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()
