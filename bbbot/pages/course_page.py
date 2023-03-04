from selenium.webdriver.common.keys import Keys
from bbbot.base.base_functions import Base
from selenium.webdriver.common.by import By

class BbCourses:
    ING_COURSE = (By.LINK_TEXT, 'The name of the class')
    ZOOM = (By.LINK_TEXT, 'Zoom Live Meeting')

    def __init__(self, driver):
        self.driver = driver
        self.methods = Base(self.driver)

    def go_ing_course(self):
        self.methods.wait_for_element(self.ING_COURSE).click()
        self.methods.wait_for_element(self.ZOOM).click()
