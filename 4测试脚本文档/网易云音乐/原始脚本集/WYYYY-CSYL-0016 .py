from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
import time

# 设置Appium服务器地址和端口
appium_server = 'http://localhost:4723/wd/hub'

# 设置desired capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'your_device_name',
    'appPackage': 'com.netease.cloudmusic',
    'appActivity': 'com.netease.cloudmusic.activity.WelcomeActivity',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

# 初始化webdriver
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 等待元素加载
    time.sleep(2)

    # 点击“其他登录方式”
    other_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView")
    other_login_button.click()

    # 勾选“我已阅读并同意”
    agree_checkbox = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 点击微信登录
    wx_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/wx")
    wx_login_button.click()

    # 等待微信登录完成
    time.sleep(10)

    # 点击播放音乐
    play_music_button = driver.find_element(AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.netease.cloudmusic:id/mixContainerRecyclerView']/android.widget.FrameLayout[4]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")
    play_music_button.click()

    # 等待音乐开始播放
    time.sleep(2)

    # 点击进入播放页面
    play_page_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/minPlayBtn")
    play_page_button.click()

    # 点击右下的三个点查看详细信息
    more_info_button = driver.find_element(AppiumBy.XPATH, "//android.widget.RelativeLayout[@resource-id='com.netease.cloudmusic:id/moreButtonContainer1']/android.widget.FrameLayout")
    more_info_button.click()

    # 验证是否显示歌曲详细信息
    song_info = driver.find_element(AppiumBy.XPATH, "//*[contains(text(), '歌曲名：')]")
    assert song_info is not None, "未显示歌曲详细信息"

finally:
    # 关闭webdriver
    driver.quit()