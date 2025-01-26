import time

from selenium.webdriver.common.by import By

from JWGLXT.website.test_case.page_object.base_page import base_page
from selenium.webdriver.support.select import Select


class home_satement_page(base_page):
    url=''
    more_studnet_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div[1]/div/a')
    attendance_student_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div[2]/div/a')
    subjcet_list=(By.XPATH,'//*[@id="subject"]')
    student_time=(By.XPATH,'//*[@id="session_year"]')
    save_button=(By.XPATH,'//*[@id="fetch_student"]')
    leave_count_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div[3]/div/a')
    confidence_subject_loc=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[1]/div[4]/div/a')
    leave_button =(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[2]/div[1]/div/div[1]/div/button[1]')
    subject_button=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[2]/div[2]/div/div[1]/div/button[1]')
    attendance_button=(By.XPATH,'/html/body/div[1]/div[1]/section/div/div[3]/div/div/div[1]/div/button[1]')



    def click_more_studnet_button(self):
        self.bp_find_element(*self.more_studnet_loc).click()

    def click_attendance_student_button(self):
        self.bp_find_element(*self.attendance_student_loc).click()


    def subject_list_select(self):
        subject_list = self.bp_find_element(*self.subjcet_list)
        select = Select(subject_list)
        select.select_by_index(0)
        print(select)
        print(*self.subjcet_list)

    def select_student_time(self):
        student_time = self.bp_find_element(*self.student_time)
        select = Select(student_time)
        select.select_by_index(1)
        print(select)
        print(*self.student_time)

    def click_save_button(self):
        self.bp_find_element(*self.save_button).click()

    def click_leave_count_button(self):
        self.bp_find_element(*self.leave_count_loc).click()

    def click_confidence_subject_button(self):
        self.bp_find_element(*self.confidence_subject_loc).click()

    def click_leave_button(self):
        self.bp_find_element(*self.leave_button).click()

    def click_subject_button(self):
        self.bp_find_element(*self. subject_button).click()

    def click_attendance_button(self):
        self.bp_find_element(*self. attendance_button).click()
def test_home_statement_page01(driver):
    home_satement_obj=home_satement_page(driver)
    home_satement_obj.click_leave_button()
    time.sleep(0.5)
    home_satement_obj.click_leave_button()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def test_home_statement_page02(driver):
    home_satement_obj=home_satement_page(driver)
    home_satement_obj.click_subject_button()
    time.sleep(0.5)
    home_satement_obj.click_subject_button()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def test_home_statement_page03(driver):
    home_satement_obj=home_satement_page(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    home_satement_obj.click_attendance_button()
    time.sleep(1)
    home_satement_obj.click_attendance_button()
    time.sleep(1)

def test_home_statement_page04(driver):
    home_satement_obj=home_satement_page(driver)
    home_satement_obj.click_attendance_student_button()
    time.sleep(1)
    home_satement_obj.subject_list_select()
    time.sleep(1)
    home_satement_obj.select_student_time()
    time.sleep(2)
    home_satement_obj.click_save_button()
    time.sleep(1)