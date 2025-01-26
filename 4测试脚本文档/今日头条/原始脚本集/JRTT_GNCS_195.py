from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0.2',
    'deviceName': 'Android Device',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashActivity',
    'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 打开今日头条App
driver.launch_app()
# 进入“头条”模块
driver.find_element_by_id("com.ss.android.article.news:id/aep").click()
# 检查右上角“发布”按钮
publish_button = driver.find_element_by_id("com.ss.android.article.news:id/aet")assert publish_button.is_displayed() and publish_button.is_enabled()

driver.quit()