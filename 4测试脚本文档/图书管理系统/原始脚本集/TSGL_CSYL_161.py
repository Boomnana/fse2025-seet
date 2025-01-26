from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 设置 WebDriver 路径
driver_path = 'path/to/your/webdriver'  # 替换为您的 WebDriver 路径

# 初始化 WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# 打开登录页面
driver.get("http://120.26.37.204:8089/library/adminLogin.html")

# 等待用户名输入框出现并输入用户名
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_input.send_keys("librarian1")

# 等待密码输入框出现并输入密码
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys("0123456")

# 等待登录按钮出现并点击
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='登录']"))
)
login_button.click()

# 等待管理员基本信息页面加载完成
admin_info_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "layout-field-box"))
)

# 获取管理员姓名、账号和邮箱
name = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '姓名')]").text
account = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '账号')]").text
email = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '邮箱')]").text

# 检查管理员基本信息是否正确
assert name == "管理员001", "姓名不匹配"
assert account == "librarian1", "账号不匹配"
assert email == "8001@qq.com", "邮箱不匹配"

# 点击修改密码按钮
change_password_button = admin_info_div.find_element(By.XPATH, ".//button[contains(text(), '修改密码')]")
change_password_button.click()

# 等待修改密码页面加载完成
change_password_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "md-content"))
)

# 检查是否跳转到修改密码页面
if change_password_div:
    print("测试通过：成功跳转到修改密码页面。")
else:
    print("测试失败：未能跳转到修改密码页面。")

# 关闭浏览器
driver.quit()