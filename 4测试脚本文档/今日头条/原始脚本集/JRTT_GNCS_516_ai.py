from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.ss.android.article.news",
    "appActivity": "com.ss.android.article.news.activity.MainActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

# 初始化WebDriver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # 测试步骤
    # 1. App起始页（点同意）
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/fs4"))
    )
    element.click()

    # 2. 点击“我的”
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[6]/android.widget.TabWidget/com.bytedance.platform.raster.viewpool.cache.compat.MeasureOnceRelativeLayout2[4]"))
    )
    element.click()

    # 3. 点击其他方式登录
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/fuo"))
    )
    element.click()

    # 4. 点击密码登录
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/dpv"))
    )
    element.click()

    # 5. 点击同意协议勾选框
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/g7p"))
    )
    element.click()

    # 6. 输入手机号
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/ib"))
    )
    element.send_keys("your_phone_number")

    # 7. 输入密码
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/ik"))
    )
    element.send_keys("your_password")

    # 8. 点击登录
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/auz"))
    )
    element.click()

    # 9. 关闭提示
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/bis"))
    )
    element.click()

    # 10. 点击设置
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/fcl"))
    )
    element.click()

    # 11. 点击编辑资料
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/ec2"))
    )
    element.click()

    # 12. 点击生日
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/eay"))
    )
    element.click()

    # 13. 选择生日年份
    year_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/jyr"))
    )
    year_element.click()
    year = "2024"  # Example year, replace with actual selection logic

    # 14. 选择生日月份
    month_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/jyo"))
    )
    month_element.click()
    month = "06"  # Example month, replace with actual selection logic

    # 15. 选择生日日期
    day_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/jyk"))
    )
    day_element.click()
    day = "15"  # Example day, replace with actual selection logic

    # 保存所选择的年份、月份、日期的text
    selected_birthday = f"{year}-{month}-{day}"

    # 15. 点击确认
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/cv"))
    )
    confirm_button.click()

    # 16. 获取更新生日信息控件的text并与保存所选择的生日的text做对比，验证是否正确
    updated_birthday_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/ime"))
    )
    assert selected_birthday == updated_birthday_element.text, "The birthday information was not updated correctly."

finally:
    driver.quit()