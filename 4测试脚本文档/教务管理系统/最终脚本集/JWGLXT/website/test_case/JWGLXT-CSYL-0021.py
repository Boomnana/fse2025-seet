from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *
from JWGLXT.website.test_case.page_object.source_page import *

class test_source(myunit.StartEnd):
    def test_source_01(self):
        test_login_page_01(self.driver,'8001@qq.com','0123456')
        test_source_page_01(self.driver)