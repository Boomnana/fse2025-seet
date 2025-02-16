from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *

class test_login(myunit.StartEnd):
    def test_login_01(self):
        test_login_page_02(self.driver, '8001@qq.com', '123456')
        self.assertEqual(login_page(self.driver).error_message_text(), '用户名或密码错误\n×')


    def test_login_02(self):
        test_login_page_02(self.driver, '9001@qq.com', '0123456')
        self.assertEqual(login_page(self.driver).error_message_text(), '用户名或密码错误\n×')
