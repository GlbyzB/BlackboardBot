from time import sleep
from bbbot.base.base_functions import Base
from selenium import webdriver
from bbbot.pages.login_page import BbLogin
from bbbot.pages.course_page import BbCourses
from bbbot.pages.zoommeetingdc import ZoomMeeting


class BbBot:

    def __init__(self):
        self.path = "\Program Files\Mozilla Firefox\geckodriver"
        self.driver = webdriver.Firefox(executable_path=self.path)
        self.driver.get("https://ku.blackboard.com/webapps/login/")
        self.driver.maximize_window()
        self.methods = Base(self.driver)
        self.bb_login_page = BbLogin(self.driver)
        self.bb_ing_course = BbCourses(self.driver)
        self.bb_join_meeting = ZoomMeeting(self.driver)


    def test_bb(self):
        self.bb_login_page.login()
        sleep(3)
        self.bb_ing_course.go_ing_course()
        sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(3)
        self.bb_join_meeting.join_meeting()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[3])
        self.driver.refresh()
        sleep(3)
        self.bb_join_meeting.open_zoom()
        sleep(5)


BbBot().test_bb()