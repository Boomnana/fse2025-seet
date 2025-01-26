from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *


class test_login(myunit.StartEnd):
    def test_login_01(self):
        test_statement_page_01(self.driver, '8001@qq.com', '0123456')
