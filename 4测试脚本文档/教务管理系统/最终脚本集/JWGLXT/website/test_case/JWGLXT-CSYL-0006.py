from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *


class test_login(myunit.StartEnd):
    def test_login_01(self):
        test_login_page_01(self.driver, '8001@qq.com', '0123456')
        self.assertEqual(login_page(self.driver).verify_name_message(), '员工 01')

    def test_login_02(self):
        test_login_page_01(self.driver, '9001@qq.com', '1234')
        self.assertEqual(login_page(self.driver).verify_name_message(), '学生 01')