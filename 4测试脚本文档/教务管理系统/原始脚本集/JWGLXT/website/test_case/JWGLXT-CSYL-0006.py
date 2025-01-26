from website.test_case.model import myunit
from website.test_case.page_object.login_page import login_page, test_login_page_01


class TestLogin(myunit.StartEnd):
    """
    测试登录功能。
    使用不同的账户（员工和学生）进行登录，并验证登录后的用户名是否正确。
    """

    def test_employee_login(self):
        """
        测试员工登录功能。
        使用员工的邮箱和密码进行登录，并验证登录后的用户名是否正确。
        """
        self._test_login('8001@qq.com', '0123456', '员工 01')

    def test_student_login(self):
        """
        测试学生登录功能。
        使用学生的邮箱和密码进行登录，并验证登录后的用户名是否正确。
        """
        self._test_login('9001@qq.com', '1234', '学生 01')

    def test_login_page_01(self, email, password, expected_name):
        """
        使用给定的邮箱和密码进行登录，并验证用户名。
        """
        test_login_page_01(self.driver, email, password)
        actual_name = login_page(self.driver).verify_name_message()
        self.assertEqual(actual_name, expected_name)

