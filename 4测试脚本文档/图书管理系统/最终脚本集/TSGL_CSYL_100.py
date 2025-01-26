from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # 导航到借阅书籍页面
    driver.get("http://120.26.37.204:8089/library/manager/01nav.jsp")

    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
    borrow_id = driver.find_element(By.NAME, "userid")
    borrow_id.send_keys("1805010204")  # 假设的借阅证号
    time.sleep(1)
    book_id = driver.find_element(By.NAME, "bookid")
    book_id.send_keys("1")  # 假设的图书编号
    time.sleep(1)
    borrow_date = driver.find_element(By.ID, "date1")
    borrow_date.clear()
    time.sleep(5)
    borrow_date.send_keys("2024-10-18 21:1:3")  # 假设的借阅日期
    time.sleep(3)

    borrow_data1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/label')
    borrow_data1.click()
    time.sleep(5)

    # 点击借阅按钮
    borrow_button = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[4]/button")
    borrow_button.click()
    time.sleep(3)

    # 等待结果弹窗出现
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    time.sleep(5)

    # 获取弹窗文本并判断结果
    alert = driver.switch_to.alert
    message = alert.text
    if "借阅成功" in message:
        print("借阅成功！")
    else:
        print("借阅失败：", message)
    alert.accept()

finally:
    # 关闭浏览器
    driver.quit()
