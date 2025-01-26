from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

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

    # 12. 点击用户名
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/eeq"))
    )
    element.click()

    # 13. 点击随机生成
    generate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/gkr"))
    )
    generate_button.click()

    # 14. 验证生成的用户名字数是否超过10
    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/hip"))
    )
    generated_username = input_element.get_attribute("text")
    assert len(generated_username) <= 10, "Generated username exceeds 10 characters"

finally:
    driver.quit()