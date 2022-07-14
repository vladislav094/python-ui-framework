from framework.features.automationpractice.locators.sing_in_page_locators import AutomationPracticeSingInPage
from framework.utils import SeleniumBase



class SingInPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.locator_sign_in_page = AutomationPracticeSingInPage

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def email_field_for_authorization(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.EMAIL_FIELD_FOR_SIGN_IN))

    @property
    def password_field(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.PASSWORD_FIELD_FOR_SIGN_IN))

    @property
    def button_for_sign_in(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.SUBMIT_BUTTON_FOR_SIGN_IN))

    @property
    def email_field_for_create(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.EMAIL_FIELD_FOR_CREATE))

    @property
    def first_name_field_for_registration(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.FIRST_NAME_FIELD))

    @property
    def last_name_field_for_registration(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.LAST_NAME_FIELD))

    @property
    def first_name_field_for_address(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.FIRST_NAME_FIELD_IN_ADDRESS))

    @property
    def last_name_field_for_address(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.LAST_NAME_FIELD_IN_ADDRESS))

    @property
    def address_field_required(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.ADDRESS_FIELD_LINE_1_IN_ADDRESS))

    @property
    def city_field(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.CITY_FIELD_IN_ADDRESS))

    @property
    def state_dropdown_list(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.STATE_DROPDOWN_LIST))

    @property
    def postal_code_field(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.POSTAL_CODE_FIELD_IN_ADDRESS))

    @property
    def country_dropdown_list(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.COUNTRY_DROPDOWN_LIST))

    @property
    def mobile_phone_field(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.MOBILE_PHONE_FIELD_IN_ADDRESS))

    @property
    def alias_for_address(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.ALIAS_ADDRESS_FIELD_IN_ADDRESS))

    @property
    def button_for_register_new_account(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.REGISTER_BUTTON))

    @property
    def button_for_create_an_account(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.SUBMIT_BUTTON_FOR_CREATE))

    @property
    def radio_button_gender_mr(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.RADIO_BUTTON_GENDER_MR))

    @property
    def link_my_account(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.LINK_MY_ACCOUNT))

    @property
    def alert_danger_authentication(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.TEXT_AUTHENTICATION_FAILED))

    @property
    def alert_create_account_mail(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_sign_in_page.TEXT_CREATE_ACCOUNT_ERROR))