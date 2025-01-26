from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.uiautomator import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置Appium连接
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "5.0")  # 根据实际设备版本调整
options.set_capability("deviceName", "YourDeviceName")  # 替换为实际设备名称
options.set_capability("appPackage", "com.netease.cloudmusic")
options.set_capability("appActivity", "com.netease.cloudmusic.activity.MainActivity")
options.set_capability("noReset", True)

driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

try:
    # 1. 打开应用
    driver.launch_app()
    time.sleep(2)  # 等待应用加载

    # 2. 进入账号页管理模块
    try:
        account_page_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.netease.cloudmusic:id/account_page_button'))
        )
        account_page_button.click()
        print("成功进入账号页。")
    except Exception as e:
        print(f"进入账号页失败：{e}")
        driver.quit()
        exit()

    # 3. 选择一个功能入口，尝试开启或关闭
    feature_id = 'com.netease.cloudmusic:id/feature_toggle'  # 替换为实际功能入口的ID

    try:
        feature_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, feature_id))
        )
        feature_element.click()  # 点击以切换功能状态
        print("点击功能入口。")

        # 检查功能入口的状态
        time.sleep(1)  # 确保状态切换有时间
        is_feature_enabled = feature_element.get_attribute('checked') == 'true'
        print(f"功能入口状态：{'开启' if is_feature_enabled else '关闭'}")

        # 预期结果检查
        expected_status = not is_feature_enabled  # 预期状态应与当前状态相反
        assert is_feature_enabled != expected_status, "功能入口状态未正确更新。"
        print("功能入口状态更新成功。")

    except Exception as e:
        print(f"功能入口操作失败：{e}")

except Exception as e:
    print(f"测试失败：{e}")

finally:
    driver.quit()
