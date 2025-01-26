from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# 设置WebDriver路径
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/adminLogin.html")
    driver.implicitly_wait(10)  # 等待页面加载完成

    # 登录
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("librarian1")
    password.send_keys("0123456")
    password.send_keys(Keys.RETURN)

    # 等待跳转到借阅图书页面
    time.sleep(5)

    # 填写借阅信息
    book_id = driver.find_element(By.NAME, "book_id")
    book_id.send_keys("123456")  # 假设的图书ID
    reader_id = driver.find_element(By.NAME, "reader_id")
    reader_id.send_keys("654321")  # 假设的读者ID

    # 选择借阅日期
    borrow_date = driver.find_element(By.NAME, "borrow_date")
    borrow_date.click()
    driver.find_element(By.XPATH, "//option[@value='2024-10-19']").click()

    # 点击借阅按钮
    borrow_button = driver.find_element(By.XPATH, "//button[text()='借阅']")
    borrow_button.click()

finally:
    # 关闭浏览器
    driver.quit()