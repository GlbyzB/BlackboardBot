from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_for_element(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def element_exist(self, locator, plural=False):
        if not plural:
            try:
                self.wait.until(ec.presence_of_element_located(locator))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(ec.presence_of_all_elements_located(locator))
                return True
            except TimeoutException:
                return False

