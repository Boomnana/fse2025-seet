# 导入必要的库
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义测试函数
def test_purchase_record_management_page():
    # 设置测试数据
    username = "采购员用户名"
    password = "采购员密码"

    # 配置WebDriver路径
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 打开超市管理系统登录页面
    driver.get("http://120.26.37.204:8088/marks/login/")  # 替换为实际的登录页面URL

    # 等待登录页面加载完成，并输入用户名和密码
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "userName")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "passWord")))

    username_input.send_keys('buyer11')
    password_input.send_keys('0123456')

    # 提交登录表单
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginFormBtn")))
    login_button.click()

    # 等待采购记录管理页面加载完成
    cgjlgl_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]")))
    cgjlgl_button.click()

    # 验证采购记录管理页面是否包含【采购】按钮和采购记录列表
    purchase_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/button")
    purchase_record_list = driver.find_element(By.CLASS_NAME, "fater-table")

    assert purchase_button.is_displayed(), "采购按钮未显示"
    assert purchase_record_list.is_displayed(), "采购记录列表未显示"

    driver.save_screenshot('CSGLXT-CSYL-0019.png')

    # 关闭浏览器
    driver.quit()


# 使用pytest运行测试
if __name__ == "__main__":
    pytest.main()