import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
def init_driver(driver_path=None):
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service)

# 等待元素加载完成
def wait_for_element(driver, by, element_name, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, element_name)))

# 处理登录流程
def login_to_site(driver, url, username, password):
    driver.get(url)
    driver.implicitly_wait(10)

    username_input = wait_for_element(driver, By.NAME, 'userName')
    password_input = wait_for_element(driver, By.NAME, 'passWord')
    login_button = wait_for_element(driver, By.ID, 'loginFormBtn')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

# 进入销售记录管理页面
def check_SalerRecordManage(driver, SalerRecordManage):
    SalerRecordManage_button = wait_for_element(driver, By.LINK_TEXT, SalerRecordManage)
    SalerRecordManage_button.click()

# 选择一个商品，进入销售清单界面
def Saler_detail(driver, CommodityDetail):
    CommodityDetail_button = wait_for_element(driver, By.XPATH, CommodityDetail)
    CommodityDetail_button.click()

# 截取屏幕截图
def take_screenshot(driver, screenshot_dir, filename):
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')

def main():
    driver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
    url = 'http://120.26.37.204:8088/marks/login/'
    username = 'saler11'
    password = '0123456'
    saler_record_manage = '销售记录管理'
    detail_button = '//*[@id="tableShow"]/table/tbody/tr[1]/td[7]/button'
    screenshot_dir = 'C:\\Users\\17586\\Desktop\\梁政宇-自动化代码\\截屏'
    screenshot_filename = 'CSGLXT-CSYL-0093.png'

    driver = None
    try:
        driver = init_driver(driver_path)
        login_to_site(driver, url, username, password)
        check_SalerRecordManage(driver, saler_record_manage)
        time.sleep(3)
        take_screenshot(driver, screenshot_dir, screenshot_filename)
    finally:
        if driver is not None:
            driver.quit()

# Pytest测试用例
class TestSalerDetail:
    @pytest.fixture
    def driver(self):
        # 初始化WebDriver
        driver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
        driver = init_driver(driver_path)
        yield driver
        driver.quit()

    def test_Saler_detail(self, driver):
        # 测试登录并检查销售清单页面
        url = 'http://120.26.37.204:8088/marks/login/'
        username = 'saler11'
        password = '0123456'
        saler_record_manage = '销售记录管理'
        detail_button = '//*[@id="tableShow"]/table/tbody/tr[1]/td[7]/button'
        screenshot_dir = 'C:\\Users\\17586\\Desktop\\lzycode\\截屏'
        screenshot_filename = 'CSGLXT-CSYL-0093.py.png'

        login_to_site(driver, url, username, password)
        check_SalerRecordManage(driver, saler_record_manage)
        Saler_detail(driver, detail_button)

        # 验证界面中是否存在“销售清单”这四个字
        sales_list_text = wait_for_element(driver, By.CSS_SELECTOR, 'body > div.detailWin.fater-model-win > div.fater-model-win-head > span:nth-child(1)', 10)
        assert sales_list_text is not None

        # 执行截屏操作
        time.sleep(3)
        take_screenshot(driver, screenshot_dir, screenshot_filename)
# 运行测试
if __name__ == '__main__':
    pytest.main()