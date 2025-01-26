from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化WebDriver，确保已经下载了对应的ChromeDriver并设置到了PATH环境变量中
driver = webdriver.Chrome()

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/adminLogin.html")

    # 等待页面加载
    time.sleep(2)

    # 找到用户名和密码输入框并输入信息
    username_input = driver.find_element(By.NAME, "username")  # 根据实际情况调整定位方式
    password_input = driver.find_element(By.NAME, "password")  # 根据实际情况调整定位方式

    username_input.send_keys("librarian1")
    password_input.send_keys("0123456")

    # 找到登录按钮并点击
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # 根据实际情况调整定位方式
    login_button.click()

    # 等待登录完成
    time.sleep(2)

    # 找到页码输入框并输入非数字页码
    page_input = driver.find_element(By.NAME, "page")  # 根据实际情况调整定位方式
    page_input.send_keys("abc")

    # 等待输入框内容消失
    time.sleep(1)

    # 验证输入框内容是否为空
    assert page_input.get_attribute("value") == "", "输入框内容没有被清空"

    # 点击确定按钮
    confirm_button = driver.find_element(By.XPATH, "//button[@type='button']")  # 根据实际情况调整定位方式
    confirm_button.click()

    # 等待一段时间，观察页面是否有响应
    time.sleep(2)

    # 这里可以添加更多的验证逻辑，例如检查页面URL是否变化，或者特定的元素是否出现
    # 例如：
    # assert "expected_url" in driver.current_url

    print("测试成功！")

except Exception as e:
    print("测试失败：", e)

finally:
    # 关闭浏览器
    driver.quit()