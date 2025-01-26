import pytest  
import os  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

class Test_Login:  
    @pytest.fixture(autouse = True)  
    def setup(self):  
        # 启动Chrome浏览器，并最大化窗口
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        # 设置隐式等待
        self.browser.implicitly_wait(10)
        # 设置显式等待
        self.wait = WebDriverWait(self.browser, 60, 0.2)
        
        # 定义页面元素的定位器
        self.username_input_loc = (By.NAME, 'userName')
        self.password_input_loc = (By.NAME, 'passWord')
        self.login_btn_loc = (By.ID, 'loginFormBtn')
        self.welcome_text_loc = (By.CSS_SELECTOR, 'body > div.fater-layout-body > blockquote')
        
        yield
        
        # 在测试结束时保存截图并关闭浏览器
        file_name = os.path.basename(__file__).split('.')[0]
        self.browser.get_screenshot_as_file(file_name + '.png')
        self.browser.quit()

    def test_salesperson_login(self):
        # 访问登录页面
        self.browser.get("http://120.26.37.204:8088/marks/login/")
        
        # 输入用户名和密码，点击登录按钮
        self.browser.find_element(*self.username_input_loc).send_keys("saler1")
        self.browser.find_element(*self.password_input_loc).send_keys("0123456")
        self.browser.find_element(*self.login_btn_loc).click()
        
        # 等待欢迎信息出现
        self.wait.until(EC.visibility_of_element_located(self.welcome_text_loc))
        welcome_text = self.browser.find_element(*self.welcome_text_loc).text
        
        # 断言欢迎信息是否包含预期文本
        assert "您好，欢迎使用超市管理系统" in welcome_text


if __name__ == "__main__": 
    # 运行测试用例
    pytest.main()
