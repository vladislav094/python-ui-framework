from framework.features.heroku.locators.frames_locator import FramesPageLocators
from framework.webpage import WebPage


class FramesPage(WebPage):
    def __init__(self, driver):
        self.locator = FramesPageLocators
        super().__init__(driver)

    def find_link_and_click(self):
        link = self.find_elt(*self.locator.LINK_IFRAME)
        self.click_elt(link)

    def find_frame_and_swithc(self):
        frame = self.find_elt(*self.locator.IFRAME_WITH_DOCUMENT)
        self.switch_frame(frame)

    def compare_text_in_frame(self):
        text = self.locator.TEXT[1]
        self.text_equal_to(text, "Your content goes here.")
