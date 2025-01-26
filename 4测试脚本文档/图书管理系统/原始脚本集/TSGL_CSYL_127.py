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

    # 等待页面加载完成
    wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='borrowed-books']")))  # 替换为实际的表格XPath

    # 点击“下一页”按钮
    next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='next-page']")))  # 替换为实际的“下一页”按钮的XPath
    next_page_button.click()

    # 验证是否跳转到第二页
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pagination']//a[@class='page-number']")))  # 替换为实际的分页导航XPath
    current_page = driver.find_element(By.XPATH, "//div[@class='pagination']//a[@class='current-page']").text  # 替换为实际的当前页码元素XPath
    assert current_page == "2", "Expected to be on page 2, but current page is {}".format(current_page)

    print("Test passed: Successfully navigated to the second page.")

except Exception as e:
    print("Test failed:", str(e))

finally:
    # 关闭浏览器
    driver.quit()