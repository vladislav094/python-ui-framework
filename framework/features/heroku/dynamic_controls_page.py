from selenium.webdriver.common.by import By

from framework.features.heroku.locators.dynamic_controls_locators import DynamicControlsPageLocators
from framework.utils import SeleniumBase


class DynamicPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.elements = DynamicControlsPageLocators

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def first_check_box(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, "//div[@id='checkbox']//input[1]"))
        return SeleniumBase(driver=self.driver, locator=(self.elements.FIRST_CHECKBOX))

    @property
    def btn_remove(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, "//*[@id='checkbox-example']/button"))
        return SeleniumBase(driver=self.driver, locator=(self.elements.BTN_REMOVE))

    @property
    def text_field(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, "//*[@id='message']"))
        return SeleniumBase(driver=self.driver, locator=(self.elements.TEXT))

    @property
    def input_field(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, "//*[@id='input-example']/input"))
        return SeleniumBase(driver=self.driver, locator=(self.elements.INPUT_FIELD))

    @property
    def btn_under_input(self):
        # return SeleniumBase(driver=self.driver, locator=(By.XPATH, "//*[@id='input-example']/button"))
        return SeleniumBase(driver=self.driver, locator=(self.elements.BTN_UNDER_INPUT))


class DynamicPage:
    def __init__(self, driver):
        self.element = DynamicPageElement(driver=driver)

    def find_check_box(self):
        ch_bx = self.element.first_check_box.find_if_visible()
        self.element.selenium.click_elt(ch_bx)

    def find_btn_remove_and_click(self):
        btn = self.element.btn_remove.find_if_visible()
        self.element.selenium.click_elt(btn)

    def wait_text_1(self):
        self.element.text_field.text_equal_to("It's gone!")

    def check_box_not_present(self):
        self.element.first_check_box.find_if_not_present()

    def find_input_and_check_disabled(self):
        input_field = self.element.input_field.find_if_visible()
        assert input_field.is_enabled() is False

    def click_btn_under_input(self):
        btn = self.element.btn_under_input.find_if_visible()
        self.element.selenium.click_elt(btn)

    def wait_text_2(self):
        self.element.text_field.text_equal_to("It's enabled!")

    def find_input_and_check_enabled(self):
        input_field = self.element.input_field.find_if_visible()
        assert input_field.is_enabled() is True
