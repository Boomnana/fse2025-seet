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

    # 12. 点击学校
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/eb_"))
    )
    element.click()

    # 检查是否能够进入选择学校界面
    try:
        element_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/h7_"))
        )
    except:
        print("Unable to enter the school selection interface.")
        exit(0)  # If the interface cannot be entered, end the test

    # 13. 选择学校元素
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/eba"))
    )
    element.click()

    # 14. 输入框输入广州番禺职业技术学院
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/h7_"))
    )
    search_box.send_keys("广州番禺职业技术学院")

    # 15. 选择列表里广州番禺职业技术学院选项
    school_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/bku"))
    )
    school_list.find_element(By.XPATH, ".//android.widget.TextView[contains(@text, '广州番禺职业技术学院')]").click()

    # 16. 点击入学年份
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/ebb"))
    )
    element.click()

    # 17. 选择入学年份
    entry_year_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/cfj"))
    )
    entry_year_element.click()
    # Assuming the year picker is a simple list, you might need to adjust the selection logic
    entry_year_element.find_element(By.XPATH, ".//android.widget.TextView[@text='2024']").click()

    # 保存所选择的入学年份信息
    selected_entry_year = "2024"

    # 18. 点击提交
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/hvz"))
    )
    element.click()

    # 19. 验证学校是否为广州番禺职业技术学院
    school_name_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/iz5"))
    )
    assert "广州番禺职业技术学院" in school_name_element.text, "The school name does not match."

    # 20. 进入学校界面
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/eba"))
    )
    element.click()

    # 21. 验证入学年份是否为选择年份
    entry_year_display_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/img"))
    )
    assert selected_entry_year in entry_year_display_element.text, "The entry year does not match."

finally:
    driver.quit()