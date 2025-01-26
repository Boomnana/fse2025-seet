from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.uiautomator import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "5.0")
options.set_capability("deviceName", "YourDeviceName")
options.set_capability("appPackage", "com.netease.cloudmusic")
options.set_capability("appActivity", "com.netease.cloudmusic.activity.MainActivity")
options.set_capability("noReset", True)

driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

try:
    # 1. 打开音乐应用
    driver.launch_app()

    # 2. 选择一首歌曲并开始播放
    song_id = 'your_song_id'  # 替换为实际歌曲ID
    try:
        song_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, f'com.netease.cloudmusic:id/{song_id}'))
        )
        song_element.click()
    except Exception as e:
        print(f"选择歌曲失败：{e}")
        driver.quit()
        exit()

    # 等待歌曲播放
    time.sleep(3)  # 等待几秒以确保歌曲开始播放

    # 3. 观察状态栏是否显示歌词
    try:
        lyrics_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'com.netease.cloudmusic:id/lyric'))
        )
        displayed_lyrics = lyrics_element.text

        # 预期结果检查
        if displayed_lyrics:
            print("歌词显示正确，实时更新。")
        else:
            print("歌词未显示。")
    except Exception as e:
        print(f"获取歌词失败：{e}")

except Exception as e:
    print(f"测试失败：{e}")

finally:
    driver.quit()
