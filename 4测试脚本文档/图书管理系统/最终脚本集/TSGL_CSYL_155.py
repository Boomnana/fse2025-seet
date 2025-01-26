from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建WebDriver对象
driver = webdriver.Chrome()

try:
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

    # 获取管理员姓名、账号和邮箱
    name = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '姓名：管理员001')]").text
    account = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '账号：librarian1')]").text
    email = admin_info_div.find_element(By.XPATH, ".//p[contains(text(), '邮箱：8001@qq.com')]").text

    # 验证基本信息是否正确
    assert name == "姓名：管理员001", "姓名不匹配"
    assert account == "账号：librarian1", "账号不匹配"
    assert email == "邮箱：8001@qq.com", "邮箱不匹配"

    print("测试成功：基本信息正确")

except Exception as e:
    print("测试失败：", e)

finally:
    # 关闭浏览器
    driver.quit()