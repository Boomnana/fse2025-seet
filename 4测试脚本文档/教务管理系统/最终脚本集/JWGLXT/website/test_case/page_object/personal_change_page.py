import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import base_page


class personal_change_page(base_page):
    url=''
    setting_loc=(By.XPATH,'/html/body/div[1]/nav/ul[2]/li/a/i')
    change_loc=(By.LINK_TEXT,'更新个人信息')
    leave_loc=(By.XPATH,'/html/body/div[1]/nav/ul[2]/li/div/a[2]')
    first_name_loc=(By.NAME,'first_name')
    last_name_loc=(By.NAME,'last_name')
    address_loc=(By.NAME,'address')
    password_loc=(By.NAME,'password')
    save_button_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div/div/div/form/div[2]/button')

    def click_setting_button(self):
        self.bp_find_element(*self.setting_loc).click()

    def click_change_button(self):
        self.bp_find_element(*self.change_loc).click()

    def click_leave_button(self):
        self.bp_find_element(*self.leave_loc).click()

    def input_first_name(self,first_name):
        self.bp_find_element(*self.first_name_loc).clear()
        self.bp_find_element(*self.first_name_loc).send_keys(first_name)

    def input_last_name(self,last_name):
        self.bp_find_element(*self.last_name_loc).clear()
        self.bp_find_element(*self.last_name_loc).send_keys(last_name)

    def input_address(self,address):
        self.bp_find_element(*self.address_loc).clear()
        self.bp_find_element(*self.address_loc).send_keys(address)

    def input_password(self,password):
        self.bp_find_element(*self.password_loc).clear()
        self.bp_find_element(*self.password_loc).send_keys(password)

    def click_save_button(self):
        self.bp_find_element(*self.save_button_loc).click()

def test_personal_change_page_01(driver):
    personal_change_page_obj=personal_change_page(driver)
    personal_change_page_obj.click_setting_button()
    time.sleep(3)
    personal_change_page_obj.click_change_button()
    time.sleep(3)
    personal_change_page_obj.input_first_name('员工')
    time.sleep(3)
    personal_change_page_obj.input_last_name('01')
    time.sleep(3)
    personal_change_page_obj.input_address('测试001')
    time.sleep(3)
    personal_change_page_obj.click_save_button()
    time.sleep(3)

def test_personal_change_page_02(driver):
    personal_change_page_obj=personal_change_page(driver)
    personal_change_page_obj.click_setting_button()
    time.sleep(3)
    personal_change_page_obj.click_leave_button()
    time.sleep(3)

def test_personal_change_page_03(driver):
    personal_change_page_obj=personal_change_page(driver)
    personal_change_page_obj.click_setting_button()
    time.sleep(3)
    personal_change_page_obj.click_change_button()
    time.sleep(3)
    personal_change_page_obj.input_first_name('1*1+-*/ab')
    time.sleep(3)
    personal_change_page_obj.input_last_name('?><+/')
    time.sleep(3)
    personal_change_page_obj.input_address('!@#$56678qQA是')
    time.sleep(3)
    personal_change_page_obj.click_save_button()
    time.sleep(3)