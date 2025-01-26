from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *
from JWGLXT.website.test_case.page_object.home_statement_page import *
class test_login(myunit.StartEnd):
    def test_home_statement_page_01(self):
        test_login_page_01(self.driver, '8001@qq.com', '0123456')
        test_home_statement_page03(self.driver)