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
# 进入相关上传页面
upload_page = driver.find_element_by_id("com.ss.android.article.news:id/afn").click()
# 检查“+”图标是否清晰可见
plus_icon = driver.find_element_by_id("com.ss.android.article.news:id/afo")assert plus_icon.is_displayed()

driver.quit()