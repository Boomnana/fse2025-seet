import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import base_page
from selenium.webdriver.common.alert import Alert

class feedback_page(base_page):
    url=''
    feedback_loc=(By.LINK_TEXT,'反馈信息')
    home_page_loc=(By.LINK_TEXT,'首页')
    feedback_message_loc=(By.NAME,'feedback_message')
    feedback_button_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[2]/button')
    feedback_message_error_empty=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/div[2]/div/div')
    feedback_message_success=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/div[2]/div/div')


    def click_feedback(self):
        self.bp_find_element(*self.feedback_loc).click()
        print('点击反馈信息')

    def input_feedback_message(self,message):
        self.bp_find_element(*self.feedback_message_loc).send_keys(message)
        print('输入反馈信息')

    def click_feedback_button(self):
        self.bp_find_element(*self.feedback_button_loc).click()


    def feedback_message_error_empty_text(self):
        contains=self.bp_find_element(*self.feedback_message_error_empty)
        print(contains.text)
        return contains.text

    def feedback_message_success_text(self):
        contains = self.bp_find_element(*self.feedback_message_success)
        print(contains.text)
        return contains.text


def test_feedback_page_01(driver):
    feedback_page_obj=feedback_page(driver)
    feedback_page_obj.click_feedback()
    time.sleep(3)
    feedback_page_obj.input_feedback_message('1')
    time.sleep(3)
    feedback_page_obj.click_feedback_button()
    time.sleep(3)
    contains=feedback_page_obj.feedback_message_error_empty_text()
    return contains

def test_feedback_page_02(driver):
    feedback_page_obj=feedback_page(driver)
    feedback_page_obj.click_feedback()
    time.sleep(3)
    feedback_page_obj.input_feedback_message('反馈测试01')
    time.sleep(3)
    feedback_page_obj.click_feedback_button()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    contains=feedback_page_obj.feedback_message_success_text()
    return contains

def test_feedback_page_03(driver):
    feedback_page_obj=feedback_page(driver)
    feedback_page_obj.click_feedback()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)