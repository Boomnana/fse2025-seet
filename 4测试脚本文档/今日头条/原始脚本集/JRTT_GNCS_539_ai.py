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

    # 12. 点击职业
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/edb"))
    )
    element.click()

    # 13. 选择职业大类
    element1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/gef"))
    )
    element1.click()
    # Assuming you select a category, you might need to adjust this step based on the actual UI

    # 14. 选择职业岗位
    element2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/a2q"))
    )
    element2.click()
    # Assuming you select a job position, you might need to adjust this step based on the actual UI

    # 保存所选择的职业大类、岗位
    selected_category = "Category Example"
    selected_job_position = "Job Position Example"

    # 15. 点击确认
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "com.ss.android.article.news:id/cv"))
    )
    confirm_button.click()

    # 16. 验证所选择的元素是否与显示的元素文本相同
    selected_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "com.ss.android.article.news:id/izz"))
    )
    assert selected_category in selected_element.text and selected_job_position in selected_element.text, "The selected job information does not match the displayed information."

finally:
    driver.quit()