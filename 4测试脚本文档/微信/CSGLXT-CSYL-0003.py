# CSGLXT_CSYL_0003.py
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Login:
    @pytest.fixture(autouse = True)
    def setup(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.wait = WebDriverWait(self.browser, 60, 0.2)
        
        self.username_input_loc = (By.NAME, 'userName')
        self.password_input_loc = (By.NAME, 'passWord')
        self.login_btn_loc = (By.ID, 'loginFormBtn')
        self.error_text_loc = (By.CLASS_NAME, 'fater-model-msg.fater-model-msg-error')
        
        yield
        file_name = os.path.basename(__file__).split('.')[0]
        self.browser.get_screenshot_as_file(file_name + '.png')
        self.browser.quit()

    def test_nonexistent_username(self):
        self.browser.get("http://120.26.37.204:8088/marks/login/")  # 替换为实际的登录页面URL
        self.browser.find_element(*self.username_input_loc).send_keys("fhihdfhih")
        self.browser.find_element(*self.password_input_loc).send_keys("0123456")
        self.browser.find_element(*self.login_btn_loc).click()
        
        # 检查是否显示了“账号不存在”的提示
        self.wait.until(expected_conditions.visibility_of_element_located(self.error_text_loc))
        error_text = self.browser.find_element(*self.error_text_loc).text
        assert "账号不存在" in error_text

# 运行测试
if __name__ == "__main__":
    pytest.main()