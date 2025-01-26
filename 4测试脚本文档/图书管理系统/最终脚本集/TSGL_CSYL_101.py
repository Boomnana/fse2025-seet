from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime, time
import time

# 创建WebDriver对象
driver = webdriver.Chrome()

try:
    # 打开登录页面
    driver.get("http://120.26.37.204:8089/library/loginManager.html")
    time.sleep(3)
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
    time.sleep(5)

    # 获取今天的日期，格式为YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 测试用例：验证借阅日期是否为当天日期
    try:
        # 找到借阅日期输入框并获取其值
        borrow_date_input = driver.find_element(By.ID, "date1")
        actual_date = borrow_date_input.get_attribute('value')

    # 比较实际日期和当天日期
        if actual_date == today_date:
            print("借阅日期为当天日期，测试通过。")
        else:
            print(f"借阅日期不为当天日期，预期：{today_date}, 实际：{actual_date}，测试失败。")
    except TimeoutException:
        print("借阅日期输入框不存在，测试失败。")

finally:
    # 关闭浏览器
    driver.quit()