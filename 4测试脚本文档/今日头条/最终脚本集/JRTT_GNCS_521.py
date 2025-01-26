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
def test():
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

    # 点击学校
    try:
      element = driver.find_element(By.ID, "com.ss.android.article.news:id/eb_")
      element.click()
    except Exception as e:
      print("点击学校发生错误：", e)

    sleep(2)

    # 进入选择学校界面
    try:
        element = driver.find_element(By.ID, "com.ss.android.article.news:id/eba")
        element.click()
        try:
            element_1 = driver.find_element(By.ID, "com.ss.android.article.news:id/h7_")
        except Exception as e:
            print("测试通过，更改学校冷却中（30天一次）", e)
            return
    except Exception as e:
        print("进入选择学校界面发生错误：", e)

    sleep(2)

    # 输入框输入
    try:
        element = driver.find_element(By.ID, "com.ss.android.article.news:id/h7_")
        element.send_keys("番禺")

    except Exception as e:
        print("进入选择学校界面发生错误：", e)

    sleep(2)

    # 列表选择
    try:
        # 定位列表
        list_element = driver.find_element(By.ID, "com.ss.android.article.news:id/bku")
        # 要查找的特定文本
        target_text = "广州番禺职业技术学院"
        # 找到所有第一级元素
        first_level_elements = list_element.find_elements(By.XPATH, ".//android.widget.LinearLayout")
        for first_level in first_level_elements:
            # 对于每个第一级元素，找到对应的第二级元素
            second_level_elements = first_level.find_elements(By.XPATH, ".//android.widget.TextView")
            for second_level in second_level_elements:
                print(second_level.text)
                if second_level.text == target_text:
                    print(f"测试通过，找到元素：{second_level.text}")
                    # 如果需要对找到的元素执行其他操作，可以在这里添加代码
                    # 例如：second_level.click()
                    break
            else:
                continue
            break  # 找到匹配的第二级元素后退出循环
        else:
            assert False, f"未找到具有特定文本'{target_text}'的元素"
    except Exception as e:
            print("发生错误：", e)

    finally:
      # 关闭WebDriver
      sleep(5)
      driver.quit()