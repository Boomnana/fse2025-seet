# 导入必要的库
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义测试函数
def test_view_product_information():
    # 设置测试数据
    username = "销售员用户名"
    password = "销售员密码"

    # 配置WebDriver路径
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 打开超市管理系统登录页面
    driver.get("http://120.26.37.204:8088/marks/login/")  # 替换为实际的登录页面URL

    # 等待登录页面加载完成，并输入用户名和密码
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "userName")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "passWord")))

    username_input.send_keys('saler11')
    password_input.send_keys('0123456')

    # 提交登录表单
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginFormBtn")))
    login_button.click()

    # 等待商品信息查看页面加载完成，并点击【商品信息查看】
    product_info_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[3]')))
    product_info_button.click()

    # 验证商品信息查看页面是否包括商品数据查询和商品信息列表
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]')))
    info_list = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tableShow"]/table')))

    assert search_box.is_displayed(), "商品数据查询框未显示"
    assert info_list.is_displayed(), "商品信息列表未显示"

    driver.save_screenshot('CSGLXT-CSYL-0037.png')

    # 关闭浏览器
    driver.quit()


# 使用pytest运行测试
if __name__ == "__main__":
    pytest.main()