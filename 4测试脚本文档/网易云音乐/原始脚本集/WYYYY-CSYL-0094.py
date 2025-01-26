from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# 初始化Appium WebDriver
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.0',  # 请根据实际设备版本修改
    'deviceName': 'Android Emulator',  # 请根据实际设备名称修改
    'appPackage': 'com.netease.cloudmusic',  # 网易云音乐的包名
    'appActivity': 'com.netease.cloudmusic.activity.SplashActivity',  # 启动Activity
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 登录网易云音乐
def login_music():
    # 假设已有登录逻辑，这里省略具体实现
    pass

# 进入消息模块
def enter_message():
    time.sleep(2)  # 等待页面加载
    # 点击左上角工具栏图标
    toolbar = driver.find_element_by_id('com.netease.cloudmusic:id/a5u')
    toolbar.click()
    time.sleep(1)  # 等待菜单展开
    # 点击“我的消息”
    message = driver.find_element_by_id('com.netease.cloudmusic:id/a5v')
    message.click()
    time.sleep(2)  # 等待消息页面加载

# 验证消息列表是否完整展示
def verify_message_list():
    message_list = driver.find_element_by_id('com.netease.cloudmusic:id/a5w')  # 消息列表的ID
    if message_list.is_displayed():
        print("消息列表完整展示，测试通过")
    else:
        print("消息列表未完整展示，测试失败")

# 主流程
def main():
    login_music()
    enter_message()
    verify_message_list()
    driver.quit()

if __name__ == '__main__':
    main()