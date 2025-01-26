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
            result = shou_ye_page.fb_add_sm()
            print("添加素材“+”按钮可视状态--->" + result)
            # 使用断言来检查方法的返回值或状态
            assert result == "True", "添加素材“+”按钮不可见"
            print("1:添加素材“+”按钮可见!")
            self.driver.quit()
        except Exception as e:
            # 如果发生异常，记录异常信息，并允许 pytest 将其标记为失败
            pytest.fail(f"添加素材“+”按钮不可见：{str(e)}")


if __name__ == '__main__':
    pytest.main()
