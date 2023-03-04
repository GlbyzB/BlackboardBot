from bbbot.base.base_functions import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ZoomMeeting:
    JOIN = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[4]/div/div[1]/a')
    LAUNCH = (By.__class__, '_1FvRrPS6')

    def __init__(self, driver):
        self.driver = driver
        self.methods = Base(self.driver)

    def join_meeting(self):
        self.methods.wait_for_element(self.JOIN).click()

    def launch_meeting(self):
        self.methods.wait_for_element(self.LAUNCH).click()

    def open_zoom(self):
        self.methods.wait_for_element(self.LAUNCH).send_keys(Keys.TAB)
        self.methods.wait_for_element(self.LAUNCH).send_keys(Keys.ENTER)

