#import necessary modules:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pom.pages.home_page import HomePage
from pom.pages.our_courses_page import OurCoursesPage
from pom.pages.post_courses_page import PostCoursesPage
from pom.pages.partners_page import PartnersPage
from pom.pages.successful_stories_page import SuccessfulStoriesPage
from pom.pages.blogs_page import BlogsPage
from pom.pages.contact_us_page import ContactUsPage
from pom.pages.admission_page import AdmissionPage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    #yield the driver
    yield driver
    #close the driver
    driver.quit()

def test_home(driver):
    home_page=HomePage(driver)
    home_page.open_home("https://www.mindrisers.com.np/")
    driver.maximize_window()
    time.sleep(1)
    # home_page.button()
    # time.sleep(1)
    home_page.scroll_page()
    time.sleep(1)
    home_page.click_interested()
    time.sleep(1)
    home_page.enter_name("Ram")
    time.sleep(1)
    home_page.enter_email("ram@gmail.com")
    time.sleep(1)
    home_page.enter_phone("9810892347")
    time.sleep(1)

def test_our_courses(driver):
    our_courses_page=OurCoursesPage(driver)
    our_courses_page.open_our_courses("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    time.sleep(1)
    our_courses_page.enter_search("QA")
    time.sleep(1)
    our_courses_page.click_search()
    time.sleep(3)
    our_courses_page.scroll_page()
    time.sleep(1)
    our_courses_page.click_qa_link()
    time.sleep(2)

def test_post_courses(driver):
    post_courses_page=PostCoursesPage(driver)
    post_courses_page.open_post_courses("https://www.mindrisers.com.np/after+2-courses")
    driver.maximize_window()
    time.sleep(1)
    post_courses_page.scroll_page()
    time.sleep(1)

def test_partners(driver):
    partners_page=PartnersPage(driver)
    partners_page.open_partners("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    time.sleep(1)
    partners_page.scroll_page()
    time.sleep(1)

def test_successful_stories(driver):
    successful_stories_page=SuccessfulStoriesPage(driver)
    successful_stories_page.open_successful_stories("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()
    time.sleep(1)
    # successful_stories_page.button()
    # time.sleep(1)
    successful_stories_page.scroll_page()
    time.sleep(1)

def test_blogs(driver):
    blogs_page=BlogsPage(driver)
    blogs_page.open_blogs("https://www.mindrisers.com.np/blogs")
    driver.maximize_window()
    time.sleep(1)
    blogs_page.scroll_page()
    time.sleep(1)

def test_contact_us(driver):
    contact_us_page=ContactUsPage(driver)
    contact_us_page.open_contact_us("https://www.mindrisers.com.np/contact-us")
    driver.maximize_window()
    time.sleep(1)
    contact_us_page.scroll_page()
    time.sleep(1)
    contact_us_page.enter_name("Ramesh")
    time.sleep(1)
    contact_us_page.enter_phone("9810827382")
    time.sleep(1)
    contact_us_page.enter_email("ramesh@gmail.com")
    time.sleep(1)
    contact_us_page.enter_subject("QA Learner")
    time.sleep(1)
    contact_us_page.enter_message("Wanted to learn QA")
    time.sleep(1)

def test_admission(driver):
    admission_page=AdmissionPage(driver)
    admission_page.open_admission("https://www.mindrisers.com.np/online-admission")
    driver.maximize_window()
    time.sleep(1)
    admission_page.scroll_page()
    time.sleep(1)
    admission_page.enter_name("Ramesh")
    time.sleep(1)
    admission_page.enter_phone("9810827382")
    time.sleep(1)
    admission_page.enter_email("ramesh@gmail.com")
    time.sleep(1)
    admission_page.enter_college("Nepal College")
    time.sleep(1)
    admission_page.enter_academic_qualification()
    time.sleep(1)
    admission_page.enter_interest()
    time.sleep(1)
    admission_page.enter_schedule()
    time.sleep(1)
    admission_page.enter_queries("This is a test for admission")
    time.sleep(1)