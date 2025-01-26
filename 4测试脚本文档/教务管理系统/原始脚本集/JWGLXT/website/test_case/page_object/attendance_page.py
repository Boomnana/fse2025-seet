import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import base_page
from selenium.webdriver.support.select import Select


class attendance_page(base_page):
    url = ''
    attendance_loc_employee = (By.LINK_TEXT, '学生考勤')
    attendance_loc_student = (By.LINK_TEXT, '查看考勤')
    subject_loc = (By.NAME, 'subject')
    session_year_loc = (By.ID, 'session_year')
    fetch_button_loc = (By.ID, 'fetch_student')
    home_page_loc = (By.LINK_TEXT, '首页')
    start_date_loc = (By.NAME, 'start_date')
    end_date_loc = (By.NAME, 'end_date')
    attendance_message=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div/div/div/div[1]/h3')

    def click_attendance_employee(self):
        self.bp_find_element(*self.attendance_loc_employee).click()
        print(*self.attendance_loc_employee)

    def click_attendance_student(self):
        self.bp_find_element(*self.attendance_loc_student).click()
        print(*self.attendance_loc_student)

    def subject_select(self):
        subject_select = self.bp_find_element(*self.subject_loc)
        select = Select(subject_select)
        select.select_by_index(0)
        print(select)
        print(*self.subject_loc)

    def select_session_year(self):
        session_year_select = self.bp_find_element(*self.session_year_loc)
        select = Select(session_year_select)
        select.select_by_index(1)
        print(select)
        print(*self.session_year_loc)

    def click_fetch_student(self):
        self.bp_find_element(*self.fetch_button_loc).click()
        print(*self.fetch_button_loc)

    def input_start_date(self, date):
        self.bp_find_element(*self.start_date_loc).send_keys(date)
        print(*self.start_date_loc)

    def input_end_date(self, date):
        self.bp_find_element(*self.end_date_loc).send_keys(date)
        print(*self.end_date_loc)

    def attendance_message_text(self):
        contains=self.bp_find_element(*self.attendance_message)
        print(contains.text)
        return contains.text


def test_attendance_page_01(driver):
    attendance_page_obj = attendance_page(driver)
    attendance_page_obj.click_attendance_employee()
    time.sleep(3)
    attendance_page_obj.select_session_year()
    time.sleep(3)
    attendance_page_obj.click_fetch_student()
    time.sleep(3)

def test_attendance_page_02(driver):
    attendance_page_obj = attendance_page(driver)
    attendance_page_obj.click_attendance_student()
    time.sleep(1)
    # attendance_page_obj.subject_select()
    # time.sleep(3)
    attendance_page_obj.input_start_date('002024-08-31')
    time.sleep(1)
    attendance_page_obj.input_end_date('002024/9/1')
    time.sleep(1)
    attendance_page_obj.click_fetch_student()
    time.sleep(1)
    contains=attendance_page_obj.attendance_message_text()
    return contains
