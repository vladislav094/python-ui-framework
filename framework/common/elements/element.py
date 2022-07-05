from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class CheckBox(WebElement):
    def get_attr_checkbox(self, attribute: str):
        if self.get_attribute("type") == "checkbox":
            print(self.get_attribute(attribute))

    def click_checkbox(self) -> None:
        if self.get_attribute("type") == "checkbox":
            self.click()

    def is_selected_checkbox(self) -> None:
        if self.get_attribute("type") == "checkbox":
            print(f"{self.is_selected()} - checkbox is selected")


class RadioButton(WebElement):
    def click_radio_btn(self):
        if self.get_attribute("type") == "radio":
            self.click()



