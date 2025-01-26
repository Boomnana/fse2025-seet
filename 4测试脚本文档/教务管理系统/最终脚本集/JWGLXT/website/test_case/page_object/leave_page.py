import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import *


class leave_page(base_page):
    url=''
    leave_loc=(By.LINK_TEXT,'请假申请')
    leave_date_loc=(By.NAME,'leave_date')
    leave_message_loc=(By.NAME,'leave_message')
    leave_button_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[2]/button')
    home_page_loc = (By.LINK_TEXT, '首页')
    leave_message_echo=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div/div/div[2]/div/div')


    def click_leave(self):
        self.bp_find_element(*self.leave_loc).click()
        print(*self.leave_loc)
        print('点击请假申请')

    def input_leave_date(self,date):
        self.bp_find_element(*self.leave_date_loc).send_keys(date)
        print('输入请假日期')

    def input_leave_message(self,message):
        self.bp_find_element(*self.leave_message_loc).send_keys(message)
        print('输入请假事由')

    def click_leave_button(self):
        self.bp_find_element(*self.leave_button_loc).click()
        print('点击请假提交')

    def leave_message_echo_text(self):
        contains=self.bp_find_element(*self.leave_message_echo)
        print(contains.text)
        return contains.text



def test_leave_page_01(driver,leave_data,leave_message):
    leave_page_obj=leave_page(driver)
    leave_page_obj.click_leave()
    time.sleep(1)
    leave_page_obj.input_leave_date(leave_data)
    time.sleep(1)
    leave_page_obj.input_leave_message(leave_message)
    time.sleep(1)
    leave_page_obj.click_leave_button()
    time.sleep(1)
    contains=leave_page_obj.leave_message_echo_text()
    return contains

def test_leave_page_02(driver,leave_data,leave_message):
    leave_page_obj=leave_page(driver)
    leave_page_obj.click_leave()
    time.sleep(1)
    leave_page_obj.input_leave_date(leave_data)
    time.sleep(1)
    leave_page_obj.input_leave_message(leave_message)
    time.sleep(1)
    leave_page_obj.click_leave_button()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    contains=leave_page_obj.leave_message_echo_text()
    return contains

def test_leave_page_03(driver):
    leave_page_obj=leave_page(driver)
    leave_page_obj.click_leave()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)