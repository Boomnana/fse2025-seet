from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.539',
    'deviceName': 'Android Device',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashActivity',
    'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 打开今日头条App
driver.launch_app()
# 进入“视频”模块
video_module = driver.find_element_by_id("com.ss.android.article.news:id/aep").click()
# 点击“收藏”
favorite_button = driver.find_element_by_id("com.ss.android.article.news:id/ah0")
favorite_button.click()
# 验证收藏功能是否正常，点击后是否有视觉变化# 这里需要实际运行脚本并观察收藏按钮的视觉变化，脚本无法自动判断

driver.quit()