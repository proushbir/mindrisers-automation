#Admission Page
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AdmissionPage:
    def __init__(self,driver):
        self.driver=driver
        self.full_name = (By.XPATH, "//input[@id='full_name']")
        self.email_field = (By.XPATH, "//input[@id='email']")
        self.phone_field = (By.XPATH, "//input[@id='mobile_no']")
        self.college_field = (By.XPATH, "//input[@id='college']")
        self.academic_status_dropdown = (By.ID, 'qualification')
        self.interest = (By.ID, 'course')
        self.preferred_schedule = (By.ID, 'shedule')
        self.queries_textbox = (By.XPATH, "//textarea[@id='question']")

    def open_admission(self,url):
        self.driver.get(url)

    def scroll_page(self):
        # set the scroll parameter
        target_y = 4000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    def enter_name(self,name):
        self.driver.find_element(*self.full_name).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def enter_college(self,college):
        self.driver.find_element(*self.college_field).send_keys(college)

    def enter_academic_qualification(self):
        academics = self.driver.find_element(*self.academic_status_dropdown)
        Select(academics).select_by_value("3")

    def enter_interest(self):
        interested_course = self.driver.find_element(*self.interest)
        Select(interested_course).select_by_value("4")

    def enter_schedule(self):
        schedule = self.driver.find_element(*self.preferred_schedule)
        Select(schedule).select_by_value("2")

    def enter_queries(self, queries):
        self.driver.find_element(*self.queries_textbox).send_keys(queries)