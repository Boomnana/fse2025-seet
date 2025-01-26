from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.attendance_page import *
from JWGLXT.website.test_case.page_object.login_page import test_login_page_01


class test_attendance(myunit.StartEnd):
    def test_attendance_01(self):
        test_login_page_01(self.driver,'9001@qq.com','1234')
        test_attendance_page_02(self.driver)
        self.assertEqual(attendance_page(self.driver).attendance_message_text(),'Finance学科的出数据')