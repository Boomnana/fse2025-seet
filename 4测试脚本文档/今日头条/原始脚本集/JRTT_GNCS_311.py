from appium import webdriverfrom appium.webdriver.common.keys import Keys

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.506',
    'deviceName': 'Android Device',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashActivity',
    'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 打开今日头条App
driver.launch_app()
# 进入“视频”模块
video_module = driver.find_element_by_id("com.ss.android.article.news:id/aep").click()
# 点击屏幕中心开始播放视频
video_play_button = driver.find_element_by_id("com.ss.android.article.news:id/afw")
video_play_button.click()
# 暂停视频
video_pause_button = driver.find_element_by_id("com.ss.android.article.news:id/afx")
video_pause_button.click()
# 再次播放视频
video_play_button.click()
# 验证暂停/播放功能是否正常# 这里需要实际运行脚本并观察视频播放情况，脚本无法自动判断功能是否正常

driver.quit()