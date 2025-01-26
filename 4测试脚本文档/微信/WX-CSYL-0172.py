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

# 进入好友聊天界面
group_chat = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.view.View')))
group_chat.click()

# 进入好友聊天信息设置页面
settings_icon = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.tencent.mm:id/eo')))
settings_icon.click()


# 测试函数
@pytest.mark.parametrize("test_data", [{}])  # 可以添加测试数据
def test_set_chat_background(test_data):
    # 点击设置当前的聊天背景
    set_background = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')))
    set_background.click()

    # 点击选择背景图
    choose_background = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')))
    choose_background.click()

    # 选择背景图1
    background_image1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.GridView/android.widget.FrameLayout[2]/android.widget.ImageView')))
    background_image1.click()

    # 截图保存
    screenshot_path = os.path.join(os.getcwd(), 'WX-CSYL-0172.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")


# 关闭WebDriver
def teardown_function():
    driver.quit()


# 运行测试
if __name__ == "__main__":
    pytest.main()
