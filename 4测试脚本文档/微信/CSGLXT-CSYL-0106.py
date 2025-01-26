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

# 选择进入购买界面
def buy(driver, CommodityDetail):
    buy_button = wait_for_element(driver, By.XPATH, CommodityDetail)
    buy_button.click()

def verify_normal_CommdoityNumber(driver, commdoity_number, buy_number, member_number):
    commdoity_number_input = wait_for_element(driver, By.NAME, 'gooId')
    buy_number_input = wait_for_element(driver, By.NAME, 'gooTotal')
    member_number_input = wait_for_element(driver, By.NAME, 'member')
    submit_button = wait_for_element(driver, By.ID, 'addFormBtn')

    commdoity_number_input.send_keys(commdoity_number)
    buy_number_input.send_keys(buy_number)
    member_number_input.send_keys(member_number)
    submit_button.click()

# 验证弹窗是否出现
# 验证弹窗是否出现
def verify_success_popup(driver, expected_text, timeout=10):
    try:
        success_popup = wait_for_element(driver, By.XPATH, "/html/body/div[9]/div[2]/div[1]", timeout)
        assert expected_text in success_popup.text
        print(f"弹窗验证成功：{expected_text}")
    except Exception as e:
        print("弹窗验证失败：", str(e))

# 截取屏幕截图
def take_screenshot(driver, screenshot_dir, filename):
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')

class TestSalerDetail:
    @pytest.fixture
    def driver(self):
        # 初始化WebDriver
        driver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
        driver = init_driver(driver_path)
        yield driver
        driver.quit()

    def test_normal_CommdoityNumber(self, driver):
        # 测试登录并检查销售记录管理页面
        url = 'http://120.26.37.204:8088/marks/login/'  # 修正了URL
        username = 'saler11'
        password = '0123456'
        saler_record_manage = '销售记录管理'
        buy_button = '/html/body/div[3]/div/div[1]/button'
        commdoity_number = '1656165092'
        buy_number = '2'
        member_number = ''
        screenshot_dir = 'C:\\Users\\17586\\Desktop\\lzycode\\截屏'
        screenshot_filename = 'CSGLXT-CSYL-0106.py.png'

        login_to_site(driver, url, username, password)
        check_SalerRecordManage(driver, saler_record_manage)
        buy(driver, buy_button)
        time.sleep(3)
        verify_normal_CommdoityNumber(driver, commdoity_number, buy_number, member_number)
        time.sleep(3)

        # 验证弹窗是否出现
        verify_success_popup(driver, "处理失败")

        # 执行截屏操作
        take_screenshot(driver, screenshot_dir, screenshot_filename)

# 运行测试
if __name__ == '__main__':
    pytest.main()