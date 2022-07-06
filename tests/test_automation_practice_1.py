import pytest

from framework.common.elements.element import CheckBox as chk_bx
from framework.features.automationpractice.main_page import MainPage
from framework.features.automationpractice.sing_in_page import SignInPage


@pytest.mark.usefixtures("set_to_hw_24")
class TestSuite:
    def test_add_to_order_and_check(self):
        main = MainPage(self.driver)
        main.open_page()
        main.check_title_main_page()
        main.scroll_page_for_items()
        main.find_item_short_and_add_to_cart()
        main.find_item_blouse_and_add_to_cart()
        main.scroll_page_to_header()
        main.go_to_cart()
        main.check_title_order_page()
        main.find_and_count_all_item_in_order()
        main.check_item_in_order()

    def test_registration_new_user(self):
        sing_in = SignInPage(self.driver)
        sing_in.open_page()
        sing_in.registration_new_email_address()
        sing_in.find_gender_Mr_and_click()
