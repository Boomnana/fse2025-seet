from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 设置Appium服务器和设备信息
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'YourDeviceName',  # 替换为你的设备名称
    'app': 'path/to/your/app.apk',  # 替换为应用路径
    'automationName': 'UiAutomator2',
}

# 初始化WebDriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def wait_and_click(locator):
    """等待元素可点击并进行点击操作"""
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"元素未找到或操作超时: {e}")


def change_appearance_settings():
    try:
        # 1. 在设置界面中选择“外观设置”选项
        wait_and_click((By.ID, 'com.example.app:id/settings'))
        wait_and_click((By.ID, 'com.example.app:id/appearance_settings'))

        # 2. 修改主题颜色为深色模式
        wait_and_click((By.XPATH, "//android.widget.TextView[@text='深色模式']"))

        # 3. 修改字体大小为“大”
        wait_and_click((By.ID, 'com.example.app:id/font_size_settings'))
        wait_and_click((By.XPATH, "//android.widget.TextView[@text='大']"))

        # 4. 确认设置并返回主界面
        wait_and_click((By.ID, 'com.example.app:id/confirm_button'))

        # 等待返回主界面
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.app:id/main_text'))
        )

        # 5. 验证外观设置是否生效（示例）
        main_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.app:id/main_text'))
        )
        print("操作成功，当前主界面文本为:", main_text.text)

    except Exception as e:
        print("操作过程中发生错误:", e)


if __name__ == "__main__":
    try:
        change_appearance_settings()
    finally:
        driver.quit()
