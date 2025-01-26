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

    # 选择搜索条件和输入图书编号

    search_condition_select = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[1]/div/div/input')  # 根据实际的下拉框名称调整
    search_condition_option = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[1]/div/dl/dd[3]')  # 根据实际的选项文本调整
    search_condition_select.click()
    time.sleep(2)
    search_condition_option.click()
    time.sleep(2)

    search_input = driver.find_element(By.ID, 'conditionValue')  # 根据实际的输入框名称调整
    search_input.send_keys('5')
    time.sleep(2)

    # 执行搜索
    search_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/button')  # 根据实际的按钮文本调整
    search_button.click()

    # 等待搜索结果
    time.sleep(3)

    # 验证搜索结果
    book_id_cells = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/table/tbody/tr/td[2]')
    all_ids_match = all(cell.text == '5' for cell in book_id_cells)

    if all_ids_match:
        print("所有搜索结果的图书编号均为5。")
    else:
        print("搜索结果中存在图书编号不为5的记录。")
#
finally:
    # 关闭浏览器
    driver.quit()
