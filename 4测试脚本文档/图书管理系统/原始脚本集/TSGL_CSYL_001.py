from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test_case(driver, username, password, expected_error_message):
    try:
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user")))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "psw")))
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='登录']")))

        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        if expected_error_message:
            error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]")))
            assert expected_error_message in error_message.text
        else:
            success_page = WebDriverWait(driver, 10).until(EC.url_contains("success_page_url"))  # Replace with actual URL
            assert success_page

        print("测试用例1通过")

    except AssertionError as e:
        print(f"测试用例1失败: {e}")
    except Exception as e:
        print(f"测试用例1错误: {e}")
    finally:
        try:
            confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]")))
            confirm_button.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error closing popup in test case 1: {e}")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://120.26.37.204:8089/library/reader/04readerFrame.jsp")
    driver.switch_to.frame("view_frame")

    run_test_case(driver, "abcd1234_", "91874", "账号长度不足")

    driver.switch_to.default_content()
    driver.quit()