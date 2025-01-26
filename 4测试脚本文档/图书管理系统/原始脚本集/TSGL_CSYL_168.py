from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 初始化WebDriver
driver = webdriver.Chrome()

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/adminLogin.html")

    # 等待登录页面加载完成
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

    # 等待管理员基本信息页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='admin-info']"))
    )

    # 点击“修改邮箱”按钮
    change_email_button = driver.find_element(By.XPATH, "//button[text()='修改邮箱']")
    change_email_button.click()

    # 等待修改邮箱页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "new_email"))
    )

    # 使用XPath定位取消按钮并点击
    cancel_button = driver.find_element(By.XPATH, "//button[contains(@class, 'md-close') and contains(text(), '取消')]")
    cancel_button.click()

    # 等待返回管理员基本信息页面
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='admin-info']"))
    )

    # 检查是否成功返回到管理员基本信息页面
    if driver.find_element(By.XPATH, "//div[@class='admin-info']").is_displayed():
        print("测试成功：成功返回到管理员基本信息页面。")
    else:
        print("测试失败：未能返回到管理员基本信息页面。")

finally:
    # 关闭浏览器
    driver.quit()