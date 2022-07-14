
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp


@pytest.mark.usefixtures("set_up_webdriver")
class TestCreatingOrders:
    def test_add_to_order_and_check(self):
        automation_practice = AutomationpracticeApp(self.driver)
        main_page = automation_practice.main_page
        automation_practice.go_to("index.php")
        main_page.check_title_main_page()
        main_page.scroll_page_for_items()
        main_page.find_item_short_and_add_to_cart()
        main_page.find_item_blouse_and_add_to_cart()
        main_page.scroll_page_to_header()
        main_page.go_to_cart()
        main_page.check_title_order_page()
        main_page.find_and_count_all_item_in_order()
        main_page.check_item_in_order()