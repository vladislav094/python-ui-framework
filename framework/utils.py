from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.5)
        self.actions = webdriver.ActionChains(driver)

    @staticmethod
    def __get_selenium_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT,
            "name": By.NAME,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag_name": By.TAG_NAME,
        }
        return locating[find_by]

    def find_if_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(
            ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def find_if_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM"""
        return self.__wait.until(
            ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def find_if_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Wait on element until it disappears"""
        return self.__wait.until(
            ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def find_are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible"""
        return self.__wait.until(
            ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM"""
        return self.__wait.until(
            ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    @staticmethod
    def get_text_from_webelements(elements: List[WebElement]) -> List[str]:
        """The input should be a list of WebElements, where we read text from each element and Return a List[String]"""
        return [element.text for element in elements]

    @staticmethod
    def get_element_by_text(elements: List[WebElement], name: str) -> WebElement:
        """The input should we a list of WebElements, from which we return a single WebElement found by it's name"""
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def hover_cursor(self, element: WebElement) -> WebElement:
        """This method moves the mouse to the middle of the element.
        The element is also scrolled into the view on performing this action."""
        return self.actions.move_to_element(element).perform()

    def window_scroll_To(self, width: int, height: int):
        """The function scrolls the page to the specified height"""
        return self.driver.execute_script(f"window.scrollTo({width}, {height})")

    def new_tab(self) -> WebElement:
        """Opening a new tab in driver"""
        return self.driver.execute_script("window.open()")

    def view_handles(self) -> List[WebElement]:
        """Getting a list of all open tabs"""
        return self.driver.window_handles

    def switch_tab(self, number: int) -> WebElement:
        return self.driver.switch_to.window(number)

    def switch_iframe(self, element: WebElement) -> WebElement:
        return self.driver.switch_to.frame(element)

    def click_elt(self, element: WebElement) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable(element)).click()

    def text_equal_to(self, locator: str, value: str) -> WebElement:
        return self.__wait.until(ec.text_to_be_present_in_element((By.XPATH, locator), value))
        # return self.__wait.until(ec.text_to_be_present_in_element((locator), value))

    def go_to_url(self, url: str) -> WebElement:
        return self.driver.get(url)

    def get_title_page(self) -> WebElement:
        return self.driver.title