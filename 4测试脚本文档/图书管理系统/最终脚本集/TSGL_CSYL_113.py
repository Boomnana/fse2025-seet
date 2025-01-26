from selenium import webdriver
from selenium.webdriver.common.by import By
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
    time.sleep(10)

    # 导航到借阅书籍页面
    driver.get("http://120.26.37.204:8089/library/manager/01nav.jsp")

    ne_page = driver.find_element(By.XPATH ,'/html/body/div/div[2]/div/ul/li[2]/a')
    ne_page.click()
    time.sleep(3)

    ne_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/ul/li[2]/dl/dd[1]/a')
    ne_page.click()
    time.sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
    time.sleep(5)


    # 点击筛选图标
    filter_icon = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]")
    filter_icon.click()
    time.sleep(2)

    # 取消勾选截止时间和归还时间
    due_date_checkbox = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/ul/li[4]/div/i")
    return_date_checkbox = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/ul/li[5]/div/i")

    due_date_checkbox.click()
    return_date_checkbox.click()

    time.sleep(2)

    re_page1 = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/button')
    time.sleep(2)

    # 检查是否成功去除截止时间和归还时间列
    due_date_column = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[1]/table")
    column_names = [col.text for col in due_date_column]

    if "截止日期" not in column_names and "归还时间" not in column_names:
        print("测试成功：已成功去除截止时间和归还时间列。")
    else:
        print("测试失败：截止时间和归还时间列仍然存在。")

finally:
    # 关闭浏览器
    driver.quit()