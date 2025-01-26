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
# 点击首页右上角的发布按钮
publish_button = driver.find_element_by_id("com.ss.android.article.news:id/aet")
publish_button.click()
# 点击“填写标题”输入框
title_input = driver.find_element_by_id("com.ss.android.article.news:id/afq")
title_input.click()
# 输入一个标题并点击其他地方或输入框外
title_input.send_keys("今日热点")
title_input.send_keys(Keys.RETURN)
# 检查标题是否保留在文本框中assert "今日热点" in title_input.text

driver.quit()