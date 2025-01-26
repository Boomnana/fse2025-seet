# CSGLXT_CSYL_0015.py
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_ChangePassword:
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
        
        self.browser.find_element(*self.username_input_loc).send_keys("buyer1")
        self.browser.find_element(*self.password_input_loc).send_keys("0123456")
        self.browser.find_element(*self.login_btn_loc).click()
        
        yield
        file_name = os.path.basename(__file__).split('.')[0]
        self.browser.get_screenshot_as_file(file_name + '.png')
        self.browser.quit()
        
    @pytest.fixture(autouse = True)
    def setup(self, login):
        self.center_loc = (By.CLASS_NAME, 'fater-user')
        self.changePwd_loc = (By.ID, 'sessionPwd')
        self.wait.until(expected_conditions.visibility_of_element_located(self.center_loc)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.changePwd_loc)).click()
        
        self.oldPwd_input_loc = (By.NAME, 'oldPwd')
        self.newPwd_input_loc = (By.NAME, 'newPwd')
        self.repPwd_input_loc = (By.NAME, 'repPwd')
        self.submit_btn_loc = (By.ID, 'updSessionPwdFormBtn')
        self.msg_text_loc = (By.XPATH, '/html/body/div[7]/div[2]/div[1]')

    def test_incorrect_old_password(self):
        self.browser.find_element(*self.oldPwd_input_loc).send_keys("wrongpassword")
        self.browser.find_element(*self.newPwd_input_loc).send_keys("newpassword")
        self.browser.find_element(*self.repPwd_input_loc).send_keys("newpassword")
        self.browser.find_element(*self.submit_btn_loc).click()
        
        # 检查是否显示了“原密码错误”的提示
        msg_text = self.browser.find_element(*self.msg_text_loc).text
        assert "原密码错误" in msg_text  # 请根据实际的错误提示文本进行调整

# 运行测试
if __name__ == "__main__":
    pytest.main()