# CSGLXT_CSYL_0017.py
import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_Logout:
    @pytest.fixture(autouse = True)
    def login(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.wait = WebDriverWait(self.browser, 60, 0.2)
        
        self.browser.get("http://120.26.37.204:8088/marks/login/")  # 替换为实际的主页URL
        self.username_input_loc = (By.NAME, 'userName')
        self.password_input_loc = (By.NAME, 'passWord')
        self.login_btn_loc = (By.ID, 'loginFormBtn')
        
        self.browser.find_element(*self.username_input_loc).send_keys("buyer2")
        self.browser.find_element(*self.password_input_loc).send_keys("0123456")
        self.browser.find_element(*self.login_btn_loc).click()
        
        yield
        file_name = os.path.basename(__file__).split('.')[0]
        self.browser.get_screenshot_as_file(file_name + '.png')
        self.browser.quit()
    
    @pytest.fixture(autouse=True)
    def setup(self, login):
        self.center_loc = (By.CLASS_NAME, 'fater-user')
        self.exitSys_loc = (By.ID, 'sessionExit')
        self.exit_btn_loc = (By.CSS_SELECTOR, 'body > div.fater-model-alert > div.fater-model-alert-body > div.fater-model-alert-btns > button.fater-btn.fater-btn-primary.fater-btn-sm')
    
    def test_logout(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.center_loc)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.exitSys_loc)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.exit_btn_loc)).click()
        
        login_url = self.browser.current_url
        assert "login" in login_url

# 运行测试
if __name__ == "__main__":
    pytest.main()