from framework.features.heroku.dynamic_controls_page import DynamicPage
from framework.features.heroku.frames_page import FramesPage


class HerokuApp:
    def __init__(self, driver):
        self.driver = driver
        self.dynamic_page = DynamicPage(self.driver)
        self.frames_page = FramesPage(self.driver)
        self.url = "http://the-internet.herokuapp.com/"

    def go_to(self, resource):
        self.driver.get(self.url + resource)
