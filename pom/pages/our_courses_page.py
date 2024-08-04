#Our Courses page
from selenium.webdriver.common.by import By

import time


class OurCoursesPage:
    def __init__(self,driver):
        self.driver=driver
        self.search_field=(By.XPATH, "//input[@name='searchTerm']")
        self.search_button=(By.XPATH,"//button[@class='btn-simple']//*[name()='svg']")
        self.qa_link=(By.XPATH,"//h3[@class='sub-header title-space-md "
                                                               "text-expanded'][normalize-space()='Quality Assurance "
                                                               "Training in Nepal']")

    def open_our_courses(self,url):
        self.driver.get(url)

    def scroll_page(self):
        # set the scroll parameter
        target_y = 500
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    def enter_search(self,search):
        self.driver.find_element(*self.search_field).send_keys(search)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def click_qa_link(self):
        self.driver.find_element(*self.qa_link).click()
