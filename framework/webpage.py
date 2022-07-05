
from framework.utils import SeleniumBase


class WebPage(SeleniumBase):
    def __init__(self, driver, find_by=None, locator=None):
        super().__init__(driver)
        self.driver = driver
        self.find_by = find_by
        self.locator = locator

    def get_nav_links_text(self, links) -> str:
        """Return all nav links text. Return format is a String with comma separated values"""
        nav_links_text = self.get_text_from_webelements(links)
        return ",".join(nav_links_text)
