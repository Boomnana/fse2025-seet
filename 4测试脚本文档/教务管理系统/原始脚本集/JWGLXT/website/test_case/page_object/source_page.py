import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import base_page
from selenium.webdriver.support.select import Select

class source_page(base_page):
    url=''
    source_loc_employee=(By.LINK_TEXT,'成绩登记')
    source_loc_student=(By.LINK_TEXT,'查看成绩')
    subject_loc=(By.ID,'subject')
    session_year_loc=(By.ID,'session_year')
    fetch_student_loc = (By.ID, 'fetch_student')
    home_page_loc = (By.LINK_TEXT, '首页')


    def click_source_employee(self):
        self.bp_find_element(*self.source_loc_employee).click()
        print(*self.source_loc_employee)

    def click_source_student(self):
        self.bp_find_element(*self.source_loc_student).click()
        print(*self.source_loc_student)

    def select_subject(self):
        subject_select=self.bp_find_element(*self.subject_loc)
        select=Select(subject_select)
        select.select_by_index(1)
        print(select)
        print(*self.subject_loc)



    def select_session_year(self):
        session_year_select = self.bp_find_element(*self.session_year_loc)
        select = Select(session_year_select)
        select.select_by_index(1)
        print(select)
        print(*self.session_year_loc)

    def fetch_student(self):
        self.bp_find_element(*self.fetch_student_loc).click()
        print(*self.fetch_student_loc)

def test_source_page_01(driver):
    source_page_obj=source_page(driver)
    source_page_obj.click_source_employee()
    time.sleep(1)
    source_page_obj.select_subject()
    time.sleep(1)
    source_page_obj.select_session_year()
    time.sleep(1)
    source_page_obj.fetch_student()
    time.sleep(1)

def test_source_page_02(driver):
    source_page_obj = source_page(driver)
    source_page_obj.click_source_student()
    time.sleep(1)