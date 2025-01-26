from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

# 设置WebDriver路径
driver_path = 'path/to/your/webdriver'

# 初始化WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# 打开登录页面
driver.get('http://120.26.37.204:8089/library/adminLogin.html')

# 等待登录页面加载完成
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
except TimeoutException:
    print("登录页面加载超时")

# 输入用户名和密码
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys('librarian1')
password.send_keys('0123456')

# 点击登录按钮
login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

# 等待页面跳转
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入借阅日期"]'))
)

# 获取今天的日期和时间，格式为YYYY-MM-DD HH:MM:SS
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 测试用例：验证借阅日期是否为当天日期且精确到时分秒
try:
    # 找到借阅日期输入框并获取其值
    borrow_date_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入借阅日期"]')
    actual_datetime = borrow_date_input.get_attribute('value')

    # 比较实际日期时间和当天日期时间
    if actual_datetime == current_datetime:
        print("借阅日期时间为当天日期时间，测试通过。")
    else:
        print(f"借阅日期时间不为当天日期时间，预期：{current_datetime}, 实际：{actual_datetime}，测试失败。")
except TimeoutException:
    print("借阅日期输入框不存在，测试失败。")

# 关闭浏览器
driver.quit()