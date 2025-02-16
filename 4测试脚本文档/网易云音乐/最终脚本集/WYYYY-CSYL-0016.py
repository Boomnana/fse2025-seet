from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Appium服务器地址和端口
appium_server = 'http://localhost:4723/wd/hub'

desired_caps = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "jbfex8prdqcuxgmr",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": "com.netease.cloudmusic.activity.MainActivity",
    "appium:unicodeKeyboard": "true",
    "appium:resetKeyboard": "true"
}

# 初始化webdriver
options = UiAutomator2Options().load_capabilities(desired_caps)

# 初始化 Appium 驱动
driver = webdriver.Remote(appium_server, options=options)

try:
    # 等待并同意用户条款进入登录页
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/agree"))
    )
    agree_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agree")
    agree_button.click()

    # 点击“其他登录方式”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView"))
    )
    other_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/thirdLoginTextView")
    other_login_button.click()

    # 等待并勾选“我已阅读并同意”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox"))
    )
    agree_checkbox = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/agreeCheckbox")
    agree_checkbox.click()

    # 点击微信登录
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.netease.cloudmusic:id/wx"))
     )
    wx_login_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/wx")
    wx_login_button.click()


    #系统权限弹窗
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]"))
    )
    always_agree_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"始终允许\"]")
    always_agree_button.click()


    # 点击播放音乐
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.netease.cloudmusic:id/mixContainerRecyclerView']/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]"))
    )
    play_music_button = driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.netease.cloudmusic:id/mixContainerRecyclerView']/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]")
    play_music_button.click()

    # 点击进入播放页面
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.netease.cloudmusic:id/minPlayBtn"))
    )
    play_page_button = driver.find_element(AppiumBy.ID, "com.netease.cloudmusic:id/minPlayBtn")
    play_page_button.click()

    # 点击右下的三个点查看详细信息
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH,
                                    "//android.widget.RelativeLayout[@resource-id='com.netease.cloudmusic:id/moreButtonContainer1']/android.widget.FrameLayout"))
    )
    more_info_button = driver.find_element(AppiumBy.XPATH,"//android.widget.RelativeLayout[@resource-id='com.netease.cloudmusic:id/moreButtonContainer1']/android.widget.FrameLayout")
    more_info_button.click()

    # 验证是否显示歌曲详细信息
    song_info = driver.find_element(AppiumBy.XPATH, "//*[contains(text(), '歌曲名：')]")
    assert song_info is not None, "未显示歌曲详细信息"

finally:
    # 关闭webdriver
    driver.quit()