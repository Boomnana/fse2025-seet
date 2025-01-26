from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *
from JWGLXT.website.test_case.page_object.personal_change_page import *


class test_personal_change(myunit.StartEnd):
    def test_personal_change_01(self):
        test_login_page_01(self.driver,'9001@qq.com','1234')
        test_personal_change_page_02(self.driver)
