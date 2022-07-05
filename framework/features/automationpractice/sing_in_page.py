from framework.common.elements.element import CheckBox as chk_bx
from framework.common.elements.element import RadioButton as radio_btn
from framework.features.automationpractice.data.data_user_for_registration import DataUserForRegistration
from framework.features.automationpractice.locators.sing_in_page_locators import AutomationPracticeSingInPage
from framework.webpage import WebPage


class SingInPage(WebPage):
    def __init__(self, driver):
        self.locator = AutomationPracticeSingInPage
        self.data = DataUserForRegistration
        self.url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        # self.url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
        super().__init__(driver)

    def open_page(self):
        self.go_to_url(self.url)

    def registration_new_email_address(self):
        field = self.find_elt(*self.locator.EMAIL_FIELD_FOR_CREATE)
        field.send_keys(self.data.EMAIL_ADDRESS)

    def find_gender_Mr_and_click(self):
        elt = self.find_elt(*self.locator.RADIO_BUTTON_GENDER_MR)
        return radio_btn.click_radio_btn(elt)
