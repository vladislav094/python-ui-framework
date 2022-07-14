from framework.features.automationpractice.locators.main_page_locators import AutomationPracticeMainPage
from framework.features.automationpractice.locators.shopping_cart_page_locators import AutomationPracticeShoppingCartPage
from framework.utils import SeleniumBase

class MainPageElement:
    def __init__(self, driver):
        self.driver = driver
        self.locator_main_page = AutomationPracticeMainPage
        self.locator_cart_page = AutomationPracticeShoppingCartPage

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def cart_with_item_short_for_order(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.CART_WITH_ITEM_SHORT_FOR_ORDER)

    @property
    def btn_add_short_item_to_cart(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.BTN_ADD_SHORT_ITEM_TO_CART))

    @property
    def btn_continue_shopping(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.BTN_CONTINUE_SHOPPING))

    @property
    def cart_with_item_blouse_for_order(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.CART_WITH_ITEM_BLOUSE_FOR_ORDER))

    @property
    def btn_add_blouse_item_to_cart(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.BTN_ADD_BLOUSE_ITEM_TO_CART))

    @property
    def btn_shopping_cart(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.BTN_SHOPPING_CART))

    @property
    def container_with_item_in_order(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_cart_page.CONTAINER_WITH_ITEM_IN_ORDER))

    @property
    def name_item_in_order_short(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_cart_page.NAME_ITEM_IN_ORDER_SHORT))

    @property
    def name_item_in_order_blouse(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_cart_page.NAME_ITEM_IN_ORDER_BLOUSE))

    @property
    def search_field(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.SEARCH_FIELD))

    @property
    def btn_submit_search(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.BTN_SUBMIT_SEARCH))

    @property
    def product_name_in_result_search(self):
        return SeleniumBase(driver=self.driver, locator=(self.locator_main_page.PRODUCT_NAME_IN_RESULT_SEARCH))