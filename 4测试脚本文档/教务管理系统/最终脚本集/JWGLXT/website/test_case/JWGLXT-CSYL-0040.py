from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.leave_page import *
from JWGLXT.website.test_case.page_object.login_page import *


class test_leave(myunit.StartEnd):

    def test_leave_02(self):
        test_login_page_01(self.driver,'8001@qq.com','0123456')
        test_leave_page_02(self.driver,'002024/10/11','员工不要当牛马')


