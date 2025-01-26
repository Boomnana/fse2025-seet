import os

import pytest

from appium import webdriver

from PageObjects.VideoModule_Page import Video_modulePage
from common.data_util import readYaml


class TestSwitch:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootpath, "config\config.yaml")
        data = readYaml(path)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data["desired_caps"])

    def test_pop(self):
        self.driver.implicitly_wait(20)
        video_page = Video_modulePage(driver=self.driver)
        try:
            text_1, text_2 = video_page.c_collect_number()
            print("收藏前收藏数--->" + text_1)
            print("收藏后收藏数--->" + text_2)
            tran_a = int(text_1)
            tran_b = int(text_2)
            expected_value1 = tran_a + 1
            expected_value2 = tran_b
            # 使用断言来检查方法的返回值或状态
            assert expected_value2 == expected_value1, "收藏数更新不及时"
            print("1:收藏数即刻更新!")
            self.driver.quit()
        except Exception as e:
            # 如果发生异常，记录异常信息，并允许 pytest 将其标记为失败
            pytest.fail(f"收藏数更新不及时：{str(e)}")


if __name__ == '__main__':
    pytest.main()
