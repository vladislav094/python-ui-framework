from framework.features.automationpractice.locators.main_page_locators import AutomationPracticeMainPage
from framework.features.automationpractice.locators.shopping_cart_page_locators import AutomationPracticeShoppingCartPage
from framework.webpage import WebPage


class MainPage(WebPage):
    def __init__(self, driver):
        self.locator = AutomationPracticeMainPage
        self.locator_cart_page = AutomationPracticeShoppingCartPage
        self.url = "http://automationpractice.com/index.php"
        super().__init__(driver)

    def open_page(self):
        self.go_to_url(self.url)

    def scroll_page_for_items(self):
        self.scroll(0, 600)

    def find_item_short_and_add_to_cart(self):
        cart_item = self.find_if_visible(*self.locator.CART_WITH_ITEM_SHORT_FOR_ORDER)
        self.hover_cursor(cart_item)
        btn_add_to_cart = self.find_if_visible(*self.locator.BTN_ADD_SHORT_ITEM_TO_CART)
        self.click_elt(btn_add_to_cart)
        btn_continue_shopping = self.find_if_visible(*self.locator.BTN_CONTINUE_SHOPPING)
        self.click_elt(btn_continue_shopping)
    def find_item_blouse_and_add_to_cart(self):

        cart_item = self.find_if_visible(*self.locator.CART_WITH_ITEM_BLOUSE_FOR_ORDER)
        self.hover_cursor(cart_item)
        btn_add_to_cart = self.find_if_visible(*self.locator.BTN_ADD_BLOUSE_ITEM_TO_CART)
        self.click_elt(btn_add_to_cart)
        btn_continue_shopping = self.find_if_visible(*self.locator.BTN_CONTINUE_SHOPPING)
        self.click_elt(btn_continue_shopping)

    def scroll_page_to_header(self):
        self.scroll(0, -600)

    def go_to_cart(self):
        btn_shopping_cart = self.find_if_visible(*self.locator.BTN_SHOPPING_CART)
        self.click_elt(btn_shopping_cart)

    def find_and_count_all_item_in_order(self):
        container = self.find_if_are_visible(*self.locator_cart_page.CONTAINER_WITH_ITEM_IN_ORDER)
        value_items_in_list = len(container)
        assert value_items_in_list == 2

    def check_item_in_order(self):
        item_1 = self.find_if_visible(*self.locator_cart_page.NAME_ITEM_IN_ORDER_SHORT)
        item_2 = self.find_if_visible(*self.locator_cart_page.NAME_ITEM_IN_ORDER_BLOUSE)
        name_1 = item_1.text
        name_2 = item_2.text
        true_name_in_site_item_1 = "Faded Short Sleeve T-shirts"
        true_name_in_site_item_2 = "Blouse"
        assert name_1 == true_name_in_site_item_1
        assert name_2 == true_name_in_site_item_2
        print(f"Item 1: {name_1}; Item 2: {name_2}")

    def check_title_main_page(self):
        title = self.get_title_page()
        assert title == "My Store"

    def check_title_order_page(self):
        title = self.get_title_page()
        assert title == "Order - My Store"
