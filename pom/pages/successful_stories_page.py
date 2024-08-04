#Successful Stories Page
import time
from selenium.webdriver.common.by import By

class SuccessfulStoriesPage:
    def __init__(self,driver):
        self.driver=driver
        #self.close_button=(By.XPATH, "//span[contains(@class,'absolute right-0 top-0 flex h-[28px] w-[28px] -translate-y-1/2 translate-x-1/2 cursor-pointer items-center justify-center rounded-full bg-red-400 font-bold text-white md:h-[32px] md:w-[32px]')]")

    def open_successful_stories(self,url):
        self.driver.get(url)

    # def button(self):
    #     self.driver.find_element(*self.close_button).click()

    def scroll_page(self):
        # set the scroll parameter
        target_y = 14000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)