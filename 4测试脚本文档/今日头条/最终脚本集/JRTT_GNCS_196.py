import os

import pytest

from PageObjects.Shouye_Page import ShouYe_Page
from appium import webdriver

from common.data_util import readYaml


class TestFabu:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootpath, "config\config.yaml")
        data = readYaml(path)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data["desired_caps"])

    def test_anni(self):
        self.driver.implicitly_wait(20)
        shou_ye_page = ShouYe_Page(driver=self.driver)
        try:
            # 假设这里有一个方法调用，我们希望确保它能够成功执行
            result = shou_ye_page.fb_page()
            expected_value = "热聊话题"
            print(result)
            # 使用断言来检查方法的返回值或状态
            assert result == expected_value, "发布按钮页面跳转操作失败"
            print("1:发布页面跳转切换成功!")
            self.driver.quit()
        except Exception as e:
            # 如果发生异常，记录异常信息，并允许 pytest 将其标记为失败
            pytest.fail(f"发布按钮页面跳转操作失败：{str(e)}")


if __name__ == '__main__':
    pytest.main()
