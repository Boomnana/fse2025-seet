from JWGLXT.website.test_case.model import myunit
from JWGLXT.website.test_case.page_object.login_page import login_page

    class TestLogin(myunit.StartEnd):
            """
            测试登录功能是否正常工作。
            """

            def test_invalid_login_credentials(self):
                """
                测试使用无效的用户名和密码登录。
                使用无效的邮箱和密码进行登录，并验证是否显示了正确的错误信息。
                """
                self._test_login_with_error('1234@qq.com', '123456', '用户名或密码错误\n×')

            def _test_login_with_error(self, email, password, expected_error):
                """
                使用给定的邮箱和密码进行登录，并验证是否显示预期的错误信息。
                """
                test_login_page_02(self.driver, email, password)
                actual_error = login_page(self.driver).error_message_text()
                self.assertEqual(actual_error, expected_error)