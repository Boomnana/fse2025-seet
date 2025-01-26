# 导入必要的库
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# 定义测试函数
def test_search_product_by_type():
    # 设置测试数据
    username = "销售员用户名"
    password = "销售员密码"
    product_type = "类型1"  # 假设商品类型为1

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

    # 等待搜索框和下拉菜单加载完成，选择商品类型进行搜索
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/select')
    element.click()
    select = Select(element)
    select.select_by_value('1656147308')
    element.click()

    # 点击搜索按钮
    earch_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[3]/button')))
    earch_button.click()

    # 等待搜索结果加载完成，并验证商品类型为1的商品是否在列表中显示
    product_list = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tableShow"]/table')))
    product_items = product_list.find_elements(By.XPATH, '//*[@id="tableShow"]/table/tbody/tr/td[6]')

    product_found = False
    for item in product_items:
        product_type = "1"
        if product_type in item.text:
            product_found = True
            break

    assert product_found, f"未查询到商品类型为 {product_type} 的商品"

    driver.save_screenshot('CSGLXT-CSYL-0042.png')

    # 关闭浏览器
    driver.quit()


# 使用pytest运行测试
if __name__ == "__main__":
    pytest.main()