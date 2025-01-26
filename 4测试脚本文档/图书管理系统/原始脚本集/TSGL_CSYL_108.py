from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置WebDriver路径
driver_path = 'path/to/your/webdriver'  # 替换为你的WebDriver路径
url = 'http://120.26.37.204:8089/library/adminLogin.html'

# 初始化WebDriver
driver = webdriver.Chrome(driver_path)

try:
    # 打开登录页面
    driver.get(url)

    # 登录
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))  # 根据实际的输入框名称调整
    )
    password_input = driver.find_element(By.NAME, 'password')  # 根据实际的输入框名称调整
    login_button = driver.find_element(By.XPATH, '//button[text()="登录"]')  # 根据实际的按钮文本调整

    username_input.send_keys('librarian1')
    password_input.send_keys('0123456')
    login_button.click()

    # 等待页面加载
    time.sleep(2)

    # 导航到借书报表页面
    borrow_report_link = driver.find_element(By.XPATH, '//a[text()="借书报表"]')  # 根据实际的链接文本调整
    borrow_report_link.click()

    # 等待借书报表页面加载
    time.sleep(2)

    # 选择搜索条件和输入图书编号
    search_condition_select = driver.find_element(By.XPATH, '//select[@name="search_condition"]')  # 根据实际的下拉框名称调整
    search_condition_option = driver.find_element(By.XPATH, '//option[text()="图书编号"]')  # 根据实际的选项文本调整
    search_condition_select.click()
    search_condition_option.click()

    search_input = driver.find_element(By.NAME, 'search_input')  # 根据实际的输入框名称调整
    search_input.send_keys('5')

    # 执行搜索
    search_button = driver.find_element(By.XPATH, '//button[text()="搜索"]')  # 根据实际的按钮文本调整
    search_button.click()

    # 等待搜索结果
    time.sleep(2)

    # 验证搜索结果
    rows = driver.find_elements(By.XPATH, '//table[@id="borrow_report_table"]/tbody/tr')  # 根据实际的表格ID调整
    for row in rows:
        book_id = row.find_element(By.XPATH, './td[2]').text  # 假设图书编号在第二列
        if book_id == '5':
            print("搜索成功，找到了图书编号为5的记录。")
        else:
            print("搜索失败，未找到图书编号为5的记录。")

finally:
    # 关闭浏览器
    driver.quit()