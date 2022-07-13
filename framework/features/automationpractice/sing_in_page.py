import time

import pytest

from framework.features.automationpractice.data.data_user_for_registration import DataUserForRegistration
from framework.features.automationpractice.locators.sing_in_page_locators import AutomationPracticeSingInPage
from framework.utils import SeleniumBase
from selenium.webdriver.common.by import By


class SingInPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.locator_sign_in_page = AutomationPracticeSingInPage
        # self.data_for_sign_in = DataUserForRegistration

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

class SignInPage:
    def __init__(self, driver):
        self.element = SingInPageElement(driver=driver)
        self.data_for_sign_in = DataUserForRegistration
        self.url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"



    def open_page(self):
        self.element.selenium.go_to_url(self.url)

    def scroll_page_to_block_your_address(self):
        self.element.selenium.scroll(0, 900)

    def authorization_in_account(self):
        email_field = self.element.email_field_for_authorization.find_if_visible()
        self.element.selenium.input(email_field, self.data_for_sign_in.SAVED_EMAIL_AFTER_REGISTRATION)
        password_field = self.element.password_field.find_if_visible()
        self.element.selenium.input(password_field, self.data_for_sign_in.SAVED_PASSWORD_AFTER_REGISTRATION)
        button_for_sign_in = self.element.button_for_sign_in.find_if_visible()
        self.element.selenium.click_elt(button_for_sign_in)

    def registration_with_invalid_email(self, email):
        email_field = self.element.email_field_for_create.find_if_visible()
        self.element.selenium.input(email_field, email)
        button_for_create_account = self.element.button_for_create_an_account.find_if_visible()
        self.element.selenium.click_elt(button_for_create_account)


    def registration_new_account(self):
        email_field = self.element.email_field_for_create.find_if_visible()
        self.element.selenium.input(email_field, self.data_for_sign_in.RANDOM_EMAIL_ADDRESS_FOR_REGISTRATION)
        button_for_create_account = self.element.button_for_create_an_account.find_if_visible()
        self.element.selenium.click_elt(button_for_create_account)

    def fill_block_with_personal_information_for_required_fields(self):
        gender_mr = self.element.radio_button_gender_mr.find_if_visible()
        self.element.selenium.click_elt(gender_mr)
        first_name_field = self.element.first_name_field_for_registration.find_if_visible()
        self.element.selenium.input(first_name_field, self.data_for_sign_in.FIRST_NAME)
        last_name_field = self.element.last_name_field_for_registration.find_if_visible()
        self.element.selenium.input(last_name_field, self.data_for_sign_in.LAST_NAME)
        password_field = self.element.password_field.find_if_visible()
        self.element.selenium.input(password_field, self.data_for_sign_in.RANDOM_PASSWORD_FOR_REGISTRATION)

    def fill_block_with_address_for_required_fields(self):
        address_field = self.element.address_field_required.find_if_visible()
        self.element.selenium.input(address_field, self.data_for_sign_in.ADDRESS_LINE_1)
        city = self.element.city_field.find_if_visible()
        self.element.selenium.input(city, self.data_for_sign_in.CITY)

        self.element.state_dropdown_list.select_in_dropdown(self.data_for_sign_in.STATE)
        self.element.country_dropdown_list.select_in_dropdown(self.data_for_sign_in.COUNTRY)

        postal_code_field = self.element.postal_code_field.find_if_visible()
        self.element.selenium.input(postal_code_field, self.data_for_sign_in.POSTAL_CODE)
        mobile_phone_field = self.element.mobile_phone_field.find_if_visible()
        self.element.selenium.input(mobile_phone_field, self.data_for_sign_in.MOBILE_PHONE)
        alias_for_address = self.element.alias_for_address.find_if_visible()
        self.element.selenium.input(alias_for_address, self.data_for_sign_in.ALIAS_ADDRESS)

    def click_button_for_register_new_account(self):
        register_button = self.element.button_for_register_new_account.find_if_visible()
        self.element.selenium.click_elt(register_button)

    def assert_my_name_in_personal_account(self):
        link_with_data_new_user = self.element.link_my_account.find_if_visible().text
        assert link_with_data_new_user == f"{self.data_for_sign_in.FIRST_NAME} {self.data_for_sign_in.LAST_NAME}"

    def assert_authentication_failed(self):
        text_with_authentication_failed = self.element.alert_danger_authentication.find_if_visible().text
        assert text_with_authentication_failed == f"Authentication failed."

    def assert_invalid_email_address(self):
        text_with_invalid_email_address = self.element.alert_create_account_mail.find_if_visible().text
        assert text_with_invalid_email_address == f"Invalid email address."
