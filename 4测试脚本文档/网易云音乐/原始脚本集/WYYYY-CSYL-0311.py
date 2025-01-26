from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.uiautomator import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置Appium连接
options = UiAutomator2Options().load_capabilities({
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "5.0",  # 根据实际版本调整
    "appPackage": "com.netease.cloudmusic",
    "appActivity": ".activity.IconChangeDefaultAlias",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
})

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
print('当前用例：设置锁屏时音乐播放的显示方式')

# 打开音乐播放软件并进入设置界面
try:
    time.sleep(5)
    driver.launch_app()

    # 进入设置界面
    menu_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/menu_icon"))
    )
    menu_icon.click()

    settings_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/settings_option"))
    )
    settings_option.click()

except Exception as e:
    print("进入设置界面发生错误：", e)

# 找到并点击“锁屏显示设置”选项
try:
    time.sleep(2)
    lock_screen_setting = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/lock_screen_setting"))
    )
    lock_screen_setting.click()

except Exception as e:
    print("点击锁屏显示设置发生错误：", e)

# 自定义锁屏时的音乐播放显示方式
try:
    time.sleep(2)
    # 示例：选择显示歌曲信息
    show_song_info_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/show_song_info_option"))
    )
    show_song_info_option.click()

    # 示例：选择显示控制按钮
    show_control_buttons_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/show_control_buttons_option"))
    )
    show_control_buttons_option.click()

    # 保存设置
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/save_button"))
    )
    save_button.click()

except Exception as e:
    print("自定义设置发生错误：", e)

# 锁屏并观察锁屏时的音乐播放显示
try:
    # 锁屏逻辑可能因设备和环境而异，通常可以使用 adb 命令锁屏
    driver.lock()  # 锁屏

    # 等待一段时间后解锁并验证显示
    time.sleep(5)
    driver.unlock()  # 解锁

    # 在这里可以添加验证显示内容的逻辑
    time.sleep(2)
    # 检查锁屏状态下的显示是否符合预期

except Exception as e:
    print("锁屏观察发生错误：", e)

finally:
    driver.quit()
