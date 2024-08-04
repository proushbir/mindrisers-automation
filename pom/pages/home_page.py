#Home Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

class HomePage:
    def __init__(self,driver):
        self.driver=driver
        # self.close_button=(By.XPATH, "//span[contains(@class,'absolute right-0 top-0 flex h-[28px] w-[28px] -translate-y-1/2 translate-x-1/2 cursor-pointer items-center justify-center rounded-full bg-red-400 font-bold text-white md:h-[32px] md:w-[32px]')]")
        self.interested_dropdown=(By.XPATH, "//*[@id='course']")
        self.name_field=(By.XPATH, "//input[@placeholder='Full Name']")
        self.email_field=(By.XPATH, "//input[@placeholder='Email']")
        self.phone_field=(By.XPATH, "//input[@placeholder='Phone Number']")

    def open_home(self,url):
        self.driver.get(url)

    # def button(self):
    #     self.driver.find_element(*self.close_button).click()

    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_interested(self):
        interested = self.driver.find_element(*self.interested_dropdown)
        Select(interested).select_by_value("6")

    def scroll_page(self):
        # set the scroll parameter
        target_y = 8000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)