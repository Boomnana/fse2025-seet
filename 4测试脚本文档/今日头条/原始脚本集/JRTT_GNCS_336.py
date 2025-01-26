from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.538',
    'deviceName': 'Android Device',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashActivity',
    'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 打开今日头条App
driver.launch_app()
# 进入“视频”模块
video_module = driver.find_element_by_id("com.ss.android.article.news:id/aep").click()
# 点击“点赞”
like_button = driver.find_element_by_id("com.ss.android.article.news:id/afy")
like_button.click()
# 点击“我的”
my_button = driver.find_element_by_id("com.ss.android.article.news:id/agx").click()
# 点击“赞过”选项卡
liked_videos = driver.find_element_by_id("com.ss.android.article.news:id/agz").click()
# 验证“赞过”列表是否出现该视频# 这里需要实际运行脚本并观察“赞过”列表，脚本无法自动判断

driver.quit()