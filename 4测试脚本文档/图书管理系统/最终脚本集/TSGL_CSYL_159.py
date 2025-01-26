import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# 点击修改名字按钮
change_name_button = admin_info_div.find_element(By.XPATH, "/html/body/fieldset/div/button[1]")
change_name_button.click()
time.sleep(3)
# 输入新名字，这里假设新名字为 "新管理员001"

new_name_input1 = driver.find_element(By.NAME,"name1")
new_name_input1.send_keys("新管理员001")
time.sleep(3)

new_name_input2 = driver.find_element(By.NAME,"name2")
new_name_input2.send_keys("新管理员002")  # 故意输入不一致的名字
time.sleep(3)

# 点击确认按钮
confirm_button = driver.find_element(By.XPATH, '//*[@id="modal-3"]/div/form/div[3]/input')
confirm_button.click()
time.sleep(3)

# 等待弹出提示信息
try:
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert_text = alert.text
    assert "修改未成功！" in alert_text, "提示信息不匹配"
    print("测试通过：修改未成功！。")
except:
    print("测试失败：没有弹出提示信息或提示信息不正确。")

# 关闭浏览器
driver.quit()