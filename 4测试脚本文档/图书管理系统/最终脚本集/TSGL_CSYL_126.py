import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    # 选择每页显示20条
    select_element = driver.find_element(By.XPATH, '//*[@id="layui-laypage-1"]/span[4]/select')
    select_element.click()
    time.sleep(5)
    option_20 = driver.find_element(By.XPATH, '//*[@id="layui-laypage-1"]/span[4]/select/option[2]')
    option_20.click()
    time.sleep(5)

    # 验证是否显示20条记录
    records = driver.find_elements(By.XPATH, "//table[@class='layui-table']/tbody/tr")
    assert len(records) == 20, "Expected 20 records, but found {}".format(len(records))

    print("测试成功: 20 records are displayed per page.")

except Exception as e:
    print("测试失败:", str(e))

finally:
    # 关闭浏览器
    driver.quit()
