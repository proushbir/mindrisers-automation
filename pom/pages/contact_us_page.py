#Contact Us Page
import time

from selenium.webdriver.common.by import By


class ContactUsPage:
    def __init__(self,driver):
        self.driver=driver
        self.full_name = (By.XPATH, "//input[@placeholder='Name']")
        self.email_field = (By.XPATH, "//input[@placeholder='Email']")
        self.phone_field = (By.XPATH, "//input[@placeholder='Phone']")
        self.subject_field = (By.XPATH, "//input[@placeholder='Subject']")
        self.message_field = (By.XPATH, "//textarea[@placeholder='Queries']")

    def open_contact_us(self,url):
        self.driver.get(url)

    def scroll_page(self):
        # set the scroll parameter
        target_y = 5000
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

    def enter_subject(self,subject):
        self.driver.find_element(*self.subject_field).send_keys(subject)

    def enter_message(self,message):
        self.driver.find_element(*self.message_field).send_keys(message)