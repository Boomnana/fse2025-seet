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

# 点击生日
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/eay")
  element.click()
except Exception as e:
  print("点击生日发生错误：", e)

sleep(2)

# 选择生日
try:
    element = driver.find_element(By.ID, "com.ss.android.article.news:id/cfj")
    element1 = driver.find_element(By.ID, "com.ss.android.article.news:id/jyr")
    element2 = driver.find_element(By.ID, "com.ss.android.article.news:id/jyo")
    element3 = driver.find_element(By.ID, "com.ss.android.article.news:id/jyk")

    bounds = element.location
    width = element.size['width']
    height = element.size['height']
    # 获取元素的文本内容并提取数字
    def extract_numbers(text):
        return re.sub(r'\D', '', text)  # 正则表达式替换非数字字符为空
    number1 = int(extract_numbers(element1.text))
    number2 = int(extract_numbers(element2.text))
    number3 = int(extract_numbers(element3.text))

    x1 = width * 0.15
    x2 = width * 0.49
    x3 = width * 0.83
    y = bounds['y'] + height * 0.33
    print(x1)
    print(x2)
    print(x3)
    print(y)

    sleep(1)
    TouchAction(driver).tap(x=x1, y=y).perform()
    sleep(1)
    TouchAction(driver).tap(x=x2, y=y).perform()
    sleep(1)
    TouchAction(driver).tap(x=x3, y=y).perform()
    sleep(1)

    element4 = driver.find_element(By.ID, "com.ss.android.article.news:id/cv")
    element4.click()
    sleep(1)

    element5 = driver.find_element(By.ID, "com.ss.android.article.news:id/ime")
    data = element5.text
    if number3 == 1:
        if number2 == 3:
            if number1 % 400 == 0 or (number1 % 4 == 0 and number1 % 100 != 0):
                relnum3 = 29
            else:
                relnum3 = 28
        elif number2 == 2 or number2 == 4 or number2 == 6 or number2 == 8 or number2 == 9 or number2 == 11 or number2 == 1:
            relnum3 = 31
        else:
            relnum3 = 30
    else:
        relnum3 = number3 - 1

    if number2 == 1:
        relnum2 = 12
    else:
        relnum2 = number2 - 1

    relnum1 = number1 - 1
    if relnum2 < 10 and relnum3 > 10:
        expected_text = f"{relnum1}-0{relnum2}-{relnum3}"
    elif relnum2 < 10 and relnum3 < 10:
        expected_text = f"{relnum1}-0{relnum2}-0{relnum3}"
    elif relnum2 > 10 and relnum3 < 10:
        expected_text = f"{relnum1}-{relnum2}-0{relnum3}"
    else:
        expected_text = f"{relnum1}-{relnum2}-{relnum3}"

    assert expected_text in data, f"选择的生日：{expected_text}与显示的生日：{data}不一致"
    print("测试通过，选择的生日已被正确显示")
except Exception as e:
    print("选择生日发生错误：", e)

finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()