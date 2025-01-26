from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 设置Appium服务器和设备信息
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'YourDeviceName',
    'app': 'path/to/your/app.apk',
    'automationName': 'UiAutomator2',
    'appWaitActivity': 'com.example.app/.MainActivity',  # 替换为你的主活动
}

# 初始化WebDriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    # 等待设置界面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'com.example.app:id/settings')))

    # 1. 在设置界面中选择“切换语言”选项
    language_switch_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'com.example.app:id/language_switch'))
    )
    language_switch_option.click()

    # 2. 等待语言列表加载并选择“简体中文”
    chinese_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='简体中文']"))
    )
    chinese_option.click()

    # 3. 确认选择并返回主界面
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'com.example.app:id/confirm_button'))
    )
    confirm_button.click()

    # 等待返回主界面
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'com.example.app:id/main_text'))
    )

    # 4. 验证语言是否切换成功
    expected_text = "欢迎使用"  # 根据实际情况更改
    main_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'com.example.app:id/main_text'))
    ).text

    assert main_text == expected_text, f"Expected text '{expected_text}', but got '{main_text}'"

except TimeoutException as e:
    print("操作超时:", e)

finally:
    driver.quit()
