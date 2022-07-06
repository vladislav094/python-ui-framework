from framework.common.elements.element import RadioButton as radio_btn
from framework.features.automationpractice.data.data_user_for_registration import DataUserForRegistration
from framework.features.automationpractice.locators.sing_in_page_locators import AutomationPracticeSingInPage
from framework.utils import SeleniumBase


class SingInPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.locator_sign_in_page = AutomationPracticeSingInPage
        self.data_for_sign_in = DataUserForRegistration

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def email_field_for_create(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.EMAIL_FIELD_FOR_CREATE))

    @property
    def radio_button_gender_mr(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.RADIO_BUTTON_GENDER_MR))

    @property
    def email_address(self):
        return self.data_for_sign_in.EMAIL_ADDRESS



class SignInPage:
    def __init__(self, driver):
        self.element = SingInPageElement(driver=driver)
        self.url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        # self.url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"

    def open_page(self):
        self.element.selenium.go_to_url(self.url)

    def registration_new_email_address(self):
        self.element.email_field_for_create.find_if_visible().send_keys(self.element.email_address)

    def find_gender_Mr_and_click(self):
        elt = self.element.radio_button_gender_mr.find_if_visible()
        return self.element.selenium.click_elt(elt)



