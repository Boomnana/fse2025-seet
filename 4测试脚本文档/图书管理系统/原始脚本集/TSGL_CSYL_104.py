from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置WebDriver路径
driver_path = 'path/to/your/webdriver'  # 替换为你的WebDriver路径
url = 'http://120.26.37.204:8089/library/adminLogin.html'

# 初始化WebDriver
driver = webdriver.Chrome(driver_path)

try:
    # 打开登录页面
    driver.get(url)

    # 登录
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))  # 根据实际的输入框名称调整
    )
    password_input = driver.find_element(By.NAME, 'password')  # 根据实际的输入框名称调整
    login_button = driver.find_element(By.XPATH, '//button[text()="登录"]')  # 根据实际的按钮文本调整

    username_input.send_keys('librarian1')
    password_input.send_keys('0123456')
    login_button.click()

    # 等待页面加载
    time.sleep(2)

    # 导航到归还图书页面
    return_book_button = driver.find_element(By.XPATH, '//a[text()="归还图书"]')  # 根据实际的链接文本调整
    return_book_button.click()

    # 等待归还图书页面加载
    time.sleep(2)

    # 输入图书编号并归还
    book_id_input = driver.find_element(By.NAME, 'book_id')  # 根据实际的输入框名称调整
    return_button = driver.find_element(By.XPATH, '//button[text()="归还"]')  # 根据实际的按钮文本调整

    book_id_input.send_keys('1')  # 假设图书编号为1
    return_button.click()

    # 等待归还结果
    time.sleep(2)

    # 验证归还结果
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="归还成功!"]'))  # 根据实际的成功消息文本调整
    )
    if success_message:
        print("图书归还成功。")
    else:
        print("图书归还失败。")

finally:
    # 关闭浏览器
    driver.quit()