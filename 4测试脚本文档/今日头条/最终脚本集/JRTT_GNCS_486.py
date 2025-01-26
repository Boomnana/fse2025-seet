from time import sleep
from appium import webdriver
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

# 点击用户名
try:
  element = driver.find_element(By.ID, "com.ss.android.article.news:id/eeq")
  element.click()
except Exception as e:
  print("点击用户名发生错误：", e)

sleep(2)

# 点击随机生成
try:
    input_element = driver.find_element(By.ID, "com.ss.android.article.news:id/hip")
    generate_button = driver.find_element(By.ID, "com.ss.android.article.news:id/gkr")
    generate_button.click()
    # 等待随机生成的用户名出现
    sleep(1)  # 根据实际情况可能需要调整等待时间
    # 获取输入框中的文本
    username = input_element.get_attribute('text')
    # 检查用户名长度是否超过20个字符
    assert len(username) <= 20, "生成的用户名长度超过了20个字符"
    print("点击随机生成测试通过：生成的用户名长度没有超过20个字符")
except AssertionError as e:
    print("点击随机生成测试失败：", e)
except Exception as e:
    print("点击随机生成发生错误：", e)


finally:
  # 关闭WebDriver
  sleep(5)
  driver.quit()
