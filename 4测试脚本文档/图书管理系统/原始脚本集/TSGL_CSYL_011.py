from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test_case(driver, username, password, expected_error_message):
    try:
        # 清空输入框
        username_input.clear()
        password_input.clear()
        time.sleep(1)

        # 输入账号和密码
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(1)

        # 点击提交按钮
        submit_button.click()
        time.sleep(1)

        # 等待错误消息元素加载完成
        if expected_error_message:
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[5]"))
            )
            assert expected_error_message in error_message.text
        else:
            # 如果没有预期错误消息，检查页面是否成功跳转
            success_page = WebDriverWait(driver, 10).until(
                EC.url_contains("success_page_url")  # 替换为实际的成功登录后的页面URL
            )
            assert success_page

        print("测试用例11通过")

    except AssertionError as e:
        print(f"测试用例11失败: {e}")
    except Exception as e:
        print(f"测试用例11错误: {e}")
    finally:
        # 尝试关闭弹窗
        try:
            # 等待确定按钮出现
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]"))
            )
            confirm_button.click()
            time.sleep(1)
        except Exception as e:
            # 如果没有找到确定按钮，忽略异常
            print(f"Error closing popup in test case 11: {e}")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://120.26.37.204:8089/library/reader/04readerFrame.jsp")
    driver.switch_to.frame("view_frame")

    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "psw")))
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='登录']"v)))

    run_test_case(driver, "178245867", "72165467321", "账号或密码错误")

    driver.switch_to.default_content()
    driver.quit()