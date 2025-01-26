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

    re_page = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/ul/li[1]/dl/dd[2]/a')
    re_page.click()
    time.sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
    time.sleep(5)

    # 查询图书是否逾期
    book_id_input = driver.find_element(By.NAME, "bookid")
    book_id_input.send_keys("1")  # 假设的图书编号
    time.sleep(1)

    query_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/button')
    query_button.click()



    # 等待查询结果
    time.sleep(2)

    return_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[7]/button')  # 根据实际的按钮文本调整
    return_button.click()


    # 等待归还结果
    time.sleep(2)

    # 获取弹窗文本并判断结果
    alert = driver.switch_to.alert
    message = alert.text
    if "归还成功！" in message:
        print("归还成功！")
    else:
        print("归还失败！", message)
        alert.accept()

finally:
    # 关闭浏览器
    driver.quit()