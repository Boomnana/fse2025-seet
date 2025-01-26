import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建WebDriver对象
driver = webdriver.Chrome()

# 打开登录页面
driver.get("http://120.26.37.204:8089/library/loginManager.html")
time.sleep(2)
driver.set_window_size(1920, 1080)
time.sleep(3)

# 登录系统
username = driver.find_element(By.NAME, "user")
password = driver.find_element(By.NAME, "psw")
username.send_keys("librarian1")
time.sleep(1)
password.send_keys("0123456")
time.sleep(1)
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/form/input[3]')
login_button.click()
time.sleep(5)

basic_info1 = driver.find_element(By.XPATH,'/html/body/div/div[1]/ul[2]/li[1]/a/span')
basic_info1.click()
time.sleep(3)
basic_info = driver.find_element(By.XPATH,'/html/body/div/div[1]/ul[2]/li[1]/dl/dd')
basic_info.click()
time.sleep(3)

driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
time.sleep(5)

# # 获取基本信息
admin_info_div = driver.find_element(By.CLASS_NAME, "layui-field-box")

# 点击修改密码按钮
change_password_button = admin_info_div.find_element(By.XPATH, "/html/body/fieldset/div/button[2]")
change_password_button.click()
time.sleep(3)

# 等待修改密码页面加载完成
change_password_div = driver.find_element(By.XPATH, '//*[@id="modal-13"]')

# 检查是否跳转到修改密码页面
if change_password_div:
    print("测试通过：成功跳转到修改密码页面。")
else:
    print("测试失败：未能跳转到修改密码页面。")
    driver.quit()

# 关闭浏览器
driver.quit()