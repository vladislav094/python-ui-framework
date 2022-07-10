import time

import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp


@pytest.mark.usefixtures("set_with_ui")
class TestSuite:
    def test_add_to_order_and_check(self):
        automationpractice = AutomationpracticeApp(self.driver)
        main_page = automationpractice.main_page
        automationpractice.go_to("index.php")
        main_page.check_title_main_page()
        main_page.scroll_page_for_items()
        main_page.find_item_short_and_add_to_cart()
        main_page.find_item_blouse_and_add_to_cart()
        main_page.scroll_page_to_header()
        main_page.go_to_cart()
        main_page.check_title_order_page()
        main_page.find_and_count_all_item_in_order()
        main_page.check_item_in_order()

    def test_registration_new_user(self):
        automationpractice = AutomationpracticeApp(self.driver)
        sign_in = automationpractice.sign_in_page
        automationpractice.go_to("index.php?controller=authentication&back=my-account")
        sign_in.registration_new_account()
        sign_in.fill_block_with_personal_information_for_required_fields()
        sign_in.scroll_page_to_block_your_address()
        sign_in.fill_block_with_address_for_required_fields()
        time.sleep(3)

