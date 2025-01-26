# 导入必要的库
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义测试函数
def test_add_purchase_record_with_invalid_product_id():
    # 设置测试数据
    username = "采购员用户名"
    password = "采购员密码"
    invalid_product_id = "-1234"
    purchase_price = "10"
    purchase_quantity = "11"

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

    # 等待采购记录管理页面加载完成，并点击【采购】按钮
    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/button')))
    purchase_button.click()

    # 等待采购信息添加页面加载完成，并输入采购信息
    product_id_input = wait.until(EC.presence_of_element_located((By.NAME, "gooId")))
    purchase_price_input = wait.until(EC.presence_of_element_located((By.NAME, "goodPrices")))
    purchase_quantity_input = wait.until(EC.presence_of_element_located((By.NAME, "gooTotal")))

    product_id_input.send_keys('-123456789')
    purchase_price_input.send_keys('100')
    purchase_quantity_input.send_keys('10')

    # 提交采购信息
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addFormBtn"]')))
    submit_button.click()

    # # 关闭提交采购信息
    # gb_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/span[2]')))
    # gb_button.click()

    # 截图提交后的页面
    driver.save_screenshot('CSGLXT-CSYL-0028.png')

    # 验证采购信息是否添加失败
    error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='error-message']")))
    assert "添加失败" in error_message.text, "采购信息添加成功，但预期应失败"

    # 关闭浏览器
    driver.quit()


# 使用pytest运行测试
if __name__ == "__main__":
    pytest.main()