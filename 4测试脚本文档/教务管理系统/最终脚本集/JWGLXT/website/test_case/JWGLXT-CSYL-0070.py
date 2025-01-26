from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import *
from JWGLXT.website.test_case.page_object.feedback_page import *
from JWGLXT.website.test_case.model.myunit import *

class TestFeedback(myunit.StartEnd):
    def test_feedback_01(self):
        # 提供 email 和 password 参数
        test_login_page_01(self.driver, '9001@qq.com', '1234')
        test_feedback_page_03(self.driver)