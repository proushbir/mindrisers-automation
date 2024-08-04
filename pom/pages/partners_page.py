#Placement Partner Page
import time

class PartnersPage:
    def __init__(self,driver):
        self.driver=driver

    def open_partners(self,url):
        self.driver.get(url)

    def scroll_page(self):
        # set the scroll parameter
        target_y = 10000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)