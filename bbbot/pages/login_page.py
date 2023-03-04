from selenium.webdriver.common.keys import Keys
from bbbot.base.base_functions import Base
from selenium.webdriver.common.by import By


class BbLogin:
    username = "username"
    password = "password"
    USERNAME = (By.ID, 'user_id')
    PASSWORD = (By.ID, 'password')
    COOKIES = (By.ID, 'agree_button')

    def __init__(self, driver):
        self.driver = driver
        self.methods = Base(self.driver)

    def login(self):
        self.methods.wait_for_element(self.COOKIES).click()
        self.methods.wait_for_element(self.USERNAME).send_keys(self.username)
        self.methods.wait_for_element(self.PASSWORD).send_keys(self.password)
        self.methods.wait_for_element(self.PASSWORD).send_keys(Keys.ENTER)
