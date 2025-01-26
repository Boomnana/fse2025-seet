import time

from selenium.webdriver.common.by import By
import selenium
from JWGLXT.website.test_case.page_object.base_page import base_page


class login_page(base_page):
    url=''
    email_loc=(By.NAME,'email')
    password_loc=(By.NAME,'password')
    login_button_loc=(By.XPATH,'/html/body/div[1]/div[2]/div/form/div[3]/button')
    name_loc = (By.XPATH, '/html/body/div[1]/aside/div/div[4]/div/div/div/div[2]/a')
    error_message=(By.XPATH,'/html/body/div[1]/div[2]/div/form/div[4]/div')


    def email_input(self,email):
        self.bp_find_element(*self.email_loc).clear()
        self.bp_find_element(*self.email_loc).send_keys(email)
        print(*self.email_loc)

    def password_input(self,password):
        self.bp_find_element(*self.password_loc).click()
        self.bp_find_element(*self.password_loc).send_keys(password)
        print(*self.password_loc)

    def login_button(self):
        self.bp_find_element(*self.login_button_loc).click()
        print(*self.login_button_loc)

    def verify_name_message(self):
        contains = self.bp_find_element(*self.name_loc)
        return contains.text

    def error_message_text(self):
        contains = self.bp_find_element(*self.error_message)
        return contains.text


def test_login_page_01(driver,email,password):
    login_page_obj=login_page(driver)
    login_page_obj.open(login_page_obj.url)
    time.sleep(1)
    login_page_obj.email_input(email)
    time.sleep(1)
    login_page_obj.password_input(password)
    time.sleep(1)
    login_page_obj.login_button()
    time.sleep(1)
    contains = login_page_obj.verify_name_message
    return contains

def test_login_page_02(driver,email,password):
    login_page_obj=login_page(driver)
    login_page_obj.open(login_page_obj.url)
    time.sleep(3)
    login_page_obj.email_input(email)
    time.sleep(3)
    login_page_obj.password_input(password)
    time.sleep(3)
    login_page_obj.login_button()
    time.sleep(3)
    contains = login_page_obj.error_message_text()
    return contains

def test_statement_page_01(driver,email,password):
    login_page_obj=login_page(driver)
    login_page_obj.open(login_page_obj.url)
    time.sleep(1)
    login_page_obj.email_input(email)
    time.sleep(1)
    login_page_obj.password_input(password)
    time.sleep(1)
    login_page_obj.login_button()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)