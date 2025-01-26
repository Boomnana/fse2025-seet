from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 设定Appium的Desired Capabilities
options = UiAutomator2Options()
options.load_capabilities({
    'platformName': 'Android',
    'platformVersion': '7.1.2',
    'deviceName': '设备名称',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
})
# 初始化WebDriver
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)

# 等待微信主界面
wait = WebDriverWait(driver, 10)

# 进入群聊界面
group_chat = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.tencent.mm:id/kic')))
group_chat.click()

# 进入群聊设置页面
settings_icon = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.tencent.mm:id/eo")))
settings_icon.click()


# 测试函数
@pytest.mark.parametrize("test_data", [{}])  # 可以添加测试数据
def test_leave_group(test_data):
    # 点击退出群聊
    leave_group = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[15]/android.widget.LinearLayout/android.widget.TextView')))
    leave_group.click()

    # 截图保存
    screenshot_path = os.path.join(os.getcwd(), 'WX-CSYL-0155.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # 确认退出
    confirm_leave = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[2]')))
    confirm_leave.click()


# 关闭WebDriver
def teardown_function():
    driver.quit()


# 运行测试
if __name__ == "__main__":
    pytest.main()
