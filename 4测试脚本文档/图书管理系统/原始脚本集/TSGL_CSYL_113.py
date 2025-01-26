from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 设置WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/adminLogin.html")

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # 输入账号和密码
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("librarian1")
    password.send_keys("0123456")

    # 提交登录表单
    driver.find_element(By.NAME, "submit").click()

    # 等待登录后页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']"))
    )

    # 点击筛选图标
    filter_icon = driver.find_element(By.XPATH, "//button[@type='button']")
    filter_icon.click()

    # 取消勾选截止时间和归还时间
    due_date_checkbox = driver.find_element(By.XPATH, "//input[@value='dueDate']")
    return_date_checkbox = driver.find_element(By.XPATH, "//input[@value='returnDate']")

    due_date_checkbox.click()
    return_date_checkbox.click()

    # 等待筛选结果更新
    WebDriverWait(driver, 10).until(
        EC.staleness_of(due_date_checkbox)
    )

    # 检查是否成功去除截止时间和归还时间列
    due_date_column = driver.find_elements(By.XPATH, "//th[@class='sorting']")
    column_names = [col.text for col in due_date_column]

    if "截止日期" not in column_names and "归还时间" not in column_names:
        print("测试成功：已成功去除截止时间和归还时间列。")
    else:
        print("测试失败：截止时间和归还时间列仍然存在。")

finally:
    # 关闭浏览器
    driver.quit()