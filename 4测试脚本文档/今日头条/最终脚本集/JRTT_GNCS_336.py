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
            text_1, text_2 = video_page.like_display_y_o()
            print("视频点赞页视频标题--->"+text_1)
            print("我的->赞过列表视频标题--->"+text_2)
            # 使用断言来检查方法的返回值或状态
            assert text_1 == text_2, "点赞的视频在用户中心赞过列表不可见"
            print("1:点赞的视频在用户中心赞过列表可见!")
            self.driver.quit()
        except Exception as e:
            # 如果发生异常，记录异常信息，并允许 pytest 将其标记为失败
            pytest.fail(f"点赞的视频在用户中心赞过列表不可见：{str(e)}")


if __name__ == '__main__':
    pytest.main()
