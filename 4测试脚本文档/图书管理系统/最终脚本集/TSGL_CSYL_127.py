import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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

    ne_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/ul/li[2]/a')
    ne_page.click()
    time.sleep(3)

    ne_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/ul/li[2]/dl/dd[1]/a')
    ne_page.click()
    time.sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[3]/iframe"))
    time.sleep(5)
    # 点击“下一页”按钮
    next_page_button = driver.find_element(By.CLASS_NAME, "layui-laypage-next")
    next_page_button.click()
    time.sleep(3)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "layui-laypage-prev"))
        )
        print("测试成功：已跳转到第二页")
    except NoSuchElementException:
        print("测试失败：无法跳转到第二页")
    except NoSuchElementException:
        print("无法找到下一页按钮")

finally:
    # 关闭浏览器
    driver.quit()
