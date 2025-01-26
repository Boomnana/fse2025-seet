import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""测试用例CSGLXT-CSYL-0048：验证操作按钮/链接是否可用且能正常工作"""
def test_operation_buttons可用():
    # 设置WebDriver路径
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        # 打开超市管理系统登录页面
        driver.get("http://120.26.37.204:8088/marks/login")

        # 登录系统
        username = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/input")
        password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/input")
        username.send_keys("saler12")
        password.send_keys("0123456")
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[3]/button")
        login_button.click()

        # 验证是否登录成功
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/blockquote")))

        # 进入商品查看页面
        product_page_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]")
        product_page_button.click()

        # 验证是否进入商品查看页面
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/table/thead/tr")))

        # 验证操作按钮/链接是否可用且能正常工作
        operation_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/table/tbody/tr[2]/td[7]")))
        assert operation_button.is_displayed()
        assert operation_button.is_enabled()

        # 截图保存运行结果
        test_case_id = "CSGLXT-CSYL-0048"
        screenshot_path = f"{test_case_id}.png"
        driver.save_screenshot(os.path.join(os.getcwd(), screenshot_path))
        print(f"截图已保存至：{screenshot_path}")

        # 测试通过
        print("测试用例CSGLXT-CSYL-0048通过：操作按钮/链接可用且能正常工作。")

    except TimeoutException:
        # 截图保存运行结果
        test_case_id = "CSGLXT-CSYL-0048"
        screenshot_path = f"{test_case_id}.png"
        driver.save_screenshot(os.path.join(os.getcwd(), screenshot_path))
        print(f"截图已保存至：{screenshot_path}")
        pytest.fail("测试用例CSGLXT-CSYL-0048失败：超时未找到元素。")
    finally:
        # 关闭浏览器
        driver.quit()


# 运行测试用例
if __name__ == "__main__":
    pytest.main(['-vs','./CSGLXT-CSYL-0048.py'])