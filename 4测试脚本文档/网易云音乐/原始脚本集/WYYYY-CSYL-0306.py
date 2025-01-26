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
    "platformVersion": "7.1.2",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": ".activity.IconChangeDefaultAlias",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
})

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
print('当前用例：桌面歌词')

# 获取屏幕宽度和高度
size = driver.get_window_size()
width = size['width']
height = size['height']
print(f"屏幕宽度: {width}, 高度: {height}")

# app起始页（点同意）
try:
    time.sleep(8)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/agree"))
    )
    element.click()
except Exception as e:
    print("起始页发生错误：", e)

time.sleep(1)

# app起始页（点允许）
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
    )
    element.click()
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击立即体验）
try:
    time.sleep(6)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/trialT"))
    )
    element.click()
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击同意）
try:
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/positiveBtn"))
    )
    element.click()
except Exception as e:
    print("app起始页发生错误：", e)

# 进入首页（点击允许）
try:
    time.sleep(8)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
    )
    element.click()
except Exception as e:
    print("app起始页发生错误：", e)

# 首页-选项
try:
    time.sleep(8)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/menu_icon"))
    )
    element.click()
except Exception as e:
    print("首页-选项发生错误：", e)

# 首页-选项-滚动到设置并点击
try:
    time.sleep(5)
    x1 = int(width * 730 / 900)
    y1 = int(height * 1540 / 1600)
    x2 = int(width * 730 / 900)
    y2 = int(height * 416 / 1600)
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()

    x3 = int(width * 676 / 900)
    y3 = int(height * 585 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
except Exception as e:
    print("首页-选项-滚动到设置点击发生错误：", e)

# 开始播放一首歌曲
try:
    time.sleep(5)
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.netease.cloudmusic:id/play_button"))
    )
    play_button.click()
    print("成功开始播放歌曲。")
except Exception as e:
    print(f"播放歌曲失败：{e}")

# 观察桌面歌词显示情况
try:
    observation_duration = 30  # 观察时间30秒
    start_time = time.time()

    while time.time() - start_time < observation_duration:
        current_lyric = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.netease.cloudmusic:id/current_lyric'))
        ).text

        progress = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.netease.cloudmusic:id/music_progress'))
        ).text

        print(f"当前歌词: {current_lyric}, 播放进度: {progress}")
        time.sleep(2)

except Exception as e:
    print(f"观察歌词显示情况失败：{e}")

finally:
    driver.quit()
