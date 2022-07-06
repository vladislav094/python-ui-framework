from selenium.webdriver.common.by import By

from framework.features.heroku.locators.frames_locator import FramesPageLocators
from framework.utils import SeleniumBase


class FramesPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.locator = FramesPageLocators

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def link_frame(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, '//*[@id="content"]/div/ul/li[2]/a'))
        return SeleniumBase(driver=self.driver, locator=(self.locator.LINK_IFRAME))

    @property
    def frame_with_document(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, '//*[@id="mce_0_ifr"]'))
        return SeleniumBase(driver=self.driver, locator=(self.locator.IFRAME_WITH_DOCUMENT))

    @property
    def text_field(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, '//*[@id="tinymce"]/p'))
        return SeleniumBase(driver=self.driver, locator=(self.locator.TEXT))


class FramesPage:
    def __init__(self, driver):
        self.element = FramesPageElement(driver=driver)

    def find_link_and_click(self):
        link = self.element.link_frame.find_if_visible()
        self.element.selenium.click_elt(link)

    def find_frame_and_switch(self):
        frame = self.element.frame_with_document.find_if_visible()
        self.element.selenium.switch_frame(frame)

    def compare_text_in_frame(self):
        self.element.text_field.text_equal_to("Your content goes here.")
