from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *
from JWGLXT.website.test_case.page_object.source_page import *

class test_source(myunit.StartEnd):
    def test_source_01(self):
        test_login_page_01(self.driver,'9001@qq.com','1234')
        test_source_page_02(self.driver)