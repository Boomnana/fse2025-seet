# 待完工
import pytest
from appium import webdriver

# 定义一个fixture来初始化和清理Appium驱动
@pytest.fixture(scope="session")
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '10',
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'automationName': 'UiAutomator2',
        'noReset': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield driver

    driver.quit()

# 定义测试类
class TestWeChat:
    # 测试启动微信
    def test_launch_wechat(self, driver):
        # 启动微信
        assert "com.tencent.mm" in driver.current_package

    # 测试打开聊天界面
    def test_open_chat(self, driver):
        # 打开聊天列表
        chat_list = driver.find_element_by_id("com.tencent.mm:id/bda")  # 聊天列表
        chat_list.click()
        # 选择第一个聊天
        first_chat = driver.find_element_by_id("com.tencent.mm:id/a5q")  # 第一个聊天
        first_chat.click()
        # 验证是否打开了聊天界面
        assert "com.tencent.mm:id/chc" in driver.page_source  # 聊天界面的某个元素ID

    # 测试发送消息
    def test_send_message(self, driver):
        # 发送消息
        chat_input = driver.find_element_by_id("com.tencent.mm:id/c6f")  # 输入框
        chat_input.send_keys("Hello, Appium!")
        send_button = driver.find_element_by_id("com.tencent.mm:id/c7b")  # 发送按钮
        send_button.click()
        # 验证消息是否发送成功
        assert "Hello, Appium!" in driver.page_source

# 运行测试
if __name__ == "__main__":
    pytest.main()