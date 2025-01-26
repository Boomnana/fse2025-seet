from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 设置WebDriver路径
driver_path = 'path/to/your/webdriver'  # 替换为你的WebDriver路径

# 初始化WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/adminLogin.html")

    # 等待登录表单元素加载
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))  # 替换为实际的用户名输入框的name或id
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))  # 替换为实际的密码输入框的name或id

    # 输入用户名和密码
    username_input.send_keys("librarian1")
    password_input.send_keys("0123456")

    # 提交表单
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))  # 替换为实际的登录按钮的XPath
    login_button.click()

    # 等待基本信息页面加载完成
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='admin-info']")))  # 替换为实际的基本信息容器的XPath

    # 获取基本信息
    name_element = driver.find_element(By.XPATH, "//div[@class='admin-info']//h1")  # 替换为实际的姓名元素XPath
    username_element = driver.find_element(By.XPATH, "//div[@class='admin-info']//p[1]")  # 替换为实际的账号元素XPath
    email_element = driver.find_element(By.XPATH, "//div[@class='admin-info']//p[2]")  # 替换为实际的邮箱元素XPath

    # 验证基本信息
    assert name_element.text == "管理员001", "Name does not match expected value"
    assert username_element.text == "账号: librarian1", "Username does not match expected value"
    assert email_element.text == "邮箱: 8001@qq.com", "Email does not match expected value"

    print("Test passed: Admin information is correct.")

except Exception as e:
    print("Test failed:", str(e))

finally:
    # 关闭浏览器
    driver.quit()