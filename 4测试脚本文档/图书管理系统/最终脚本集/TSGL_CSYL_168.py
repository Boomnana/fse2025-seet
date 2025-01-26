import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
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

    basic_info1 = driver.find_element(By.XPATH, '/html/body/div/div[1]/ul[2]/li[1]/a/span')
    basic_info1.click()
    time.sleep(3)
    basic_info = driver.find_element(By.XPATH, '/html/body/div/div[1]/ul[2]/li[1]/dl/dd')
    basic_info.click()
    time.sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
    time.sleep(5)

    # # 获取基本信息
    admin_info_div = driver.find_element(By.CLASS_NAME, "layui-field-box")

    # 点击修改邮箱按钮
    change_password_button = admin_info_div.find_element(By.XPATH, "/html/body/fieldset/div/button[3]")
    change_password_button.click()
    time.sleep(5)

    # 定位包含取消按钮的父级div元素
    parent_div = driver.find_element(By.CSS_SELECTOR, ".md-modal.md-effect-13.md-show")

    # 在父级div元素中定位取消按钮
    cancel_button = parent_div.find_element(By.XPATH, ".//button[contains(text(), '取消')]")
    cancel_button.click()
    time.sleep(3)

    # 等待返回管理员基本信息页面
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "layui-field-box"))
    )

    # 检查是否成功返回到管理员基本信息页面
    if driver.find_element(By.CLASS_NAME, "layui-field-box").is_displayed():
        print("测试成功：成功返回到管理员基本信息页面。")
    else:
        print("测试失败：未能返回到管理员基本信息页面。")

finally:
    # 关闭浏览器
    driver.quit()