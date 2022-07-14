from framework.features.automationpractice.property_locators.main_page_property import MainPageElement
from framework.features.automationpractice.data.data_product import DataProduct



class MainPage:
    def __init__(self, driver):
        self.element = MainPageElement(driver=driver)
        self.data_product = DataProduct

    def scroll_page_for_items(self):
        self.element.selenium.scroll(0, 600)

    def find_item_short_and_add_to_cart(self):
        cart_item = self.element.cart_with_item_short_for_order.find_if_visible()
        self.element.selenium.hover_cursor(cart_item)
        btn_add_to_cart = self.element.btn_add_short_item_to_cart.find_if_visible()
        self.element.selenium.click_elt(btn_add_to_cart)
        btn_continue_shopping = self.element.btn_continue_shopping.find_if_visible()
        self.element.selenium.click_elt(btn_continue_shopping)

    def find_item_blouse_and_add_to_cart(self):
        cart_item = self.element.cart_with_item_blouse_for_order.find_if_visible()
        self.element.selenium.hover_cursor(cart_item)
        btn_add_to_cart = self.element.btn_add_blouse_item_to_cart.find_if_visible()
        self.element.selenium.click_elt(btn_add_to_cart)
        btn_continue_shopping = self.element.btn_continue_shopping.find_if_visible()
        self.element.selenium.click_elt(btn_continue_shopping)

    def scroll_page_to_header(self):
        self.element.selenium.scroll(0, -600)

    def go_to_cart(self):
        btn_shopping_cart = self.element.btn_shopping_cart.find_if_visible()
        self.element.selenium.click_elt(btn_shopping_cart)

    def find_and_count_all_item_in_order(self):
        container = self.element.container_with_item_in_order.find_if_are_visible()
        value_items_in_list = len(container)
        assert value_items_in_list == 2

    def check_item_in_order(self):
        item_1 = self.element.name_item_in_order_short.find_if_visible().text
        item_2 = self.element.name_item_in_order_blouse.find_if_visible().text
        assert item_1 == self.data_product.PRODUCT_WITH_NAME_FADED_SHORT_SLEEVE
        assert item_2 == self.data_product.PRODUCT_WITH_NAME_BLOUSE
        print(f"Item 1: {item_1}; Item 2: {item_2}")

    def check_title_main_page(self):
        title = self.element.selenium.get_title_page()
        assert title == "My Store"

    def check_title_order_page(self):
        title = self.element.selenium.get_title_page()
        assert title == "Order - My Store"

    def fill_search_field_and_assert_result(self):
        search_field = self.element.search_field.find_if_visible()
        self.element.selenium.input(search_field, self.data_product.PRODUCT_WITH_NAME_BLOUSE)
        btn_submit_search = self.element.btn_submit_search.find_if_visible()
        self.element.selenium.click_elt(btn_submit_search)
        product_name_in_result_search = self.element.product_name_in_result_search.find_if_visible().text
        assert product_name_in_result_search == self.data_product.PRODUCT_WITH_NAME_BLOUSE



