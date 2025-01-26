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

    # 找到页码输入框并输入非数字页码
    # page_input = driver.execute_script("return document.querySelector('.layui-input')")# 假设页码输入框的name属性为"page"
    page_input = driver.find_element(By.XPATH, "//div[@class='layui-box layui-laypage layui-laypage-default']//input[@class='layui-input']")
    page_input.clear()
    time.sleep(4)
    page_input.send_keys("abc")
    time.sleep(3)

    assert page_input.get_attribute("value") == "", "输入框内容没有被清空"

    # 点击确定按钮
    confirm_button = driver.find_element(By.CLASS_NAME, "layui-laypage-btn")
    confirm_button.click()

    # 等待一段时间，观察页面是否有响应
    time.sleep(2)

    print("测试成功！")

except Exception as e:
    print("测试失败：", e)

finally:
    driver.quit()