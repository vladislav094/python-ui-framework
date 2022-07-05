from framework.features.heroku.locators.dynamic_controls_locators import DynamicControlsPageLocators
from framework.webpage import WebPage


class DynamicPage(WebPage):
    def __init__(self, driver):
        self.locator = DynamicControlsPageLocators
        self.url = "http://the-internet.herokuapp.com/dynamic_controls"
        super().__init__(driver)

    def open_page(self):
        self.go_to_url(self.url)

    def find_check_box(self):
        return self.find_elt(*self.locator.FIRST_CHECKBOX)

    def find_btn_remove_and_click(self):
        btn = self.find_elt(*self.locator.BTN_REMOVE)
        self.click_elt(btn)

    def wait_text_1(self):
        text = self.locator.TEXT[1]
        self.text_equal_to(text, "It's gone")

    def check_box_not_present(self):
        return self.find_if_not_present(*self.locator.FIRST_CHECKBOX)

    def find_input_and_check_disabled(self):
        input_field = self.find_elt(*self.locator.INPUT_FIELD)
        assert input_field.is_enabled() is False

    def click_btn_under_input(self):
        btn = self.find_elt(*self.locator.BTN_UNDER_INPUT)
        self.click_elt(btn)

    def wait_text_2(self):
        text_2 = self.locator.TEXT[1]
        self.text_equal_to(text_2, "It's enabled!")

    def find_input_and_check_enabled(self):
        input_field = self.find_elt(*self.locator.INPUT_FIELD)
        assert input_field.is_enabled() is True
