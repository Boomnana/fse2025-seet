from selenium import webdriver
def getChromeDriver():
    # 创建ChromeOptions对象
    chrome_options = webdriver.ChromeOptions()

    # 禁用图形加速
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    # driver= webdriver.Chrome()
    return driver


