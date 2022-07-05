from selenium.webdriver.common.by import By


class AutomationPracticeShoppingCartPage:
    FRAME_LAYER_CART = (By.XPATH, "//*[@id='layer_cart']/div[1]")
    CONTAINER_WITH_ITEM_IN_ORDER = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr')
    NAME_ITEM_IN_ORDER_SHORT = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr[1]/td/p/a')
    NAME_ITEM_IN_ORDER_BLOUSE = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr[2]/td/p/a')

    """All button"""
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@id="center_column"]/p[2]/a[2]')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    PROCEED_TO_CHECKOUT_BUTTON_IN_ADDRESS_TAB = (By.XPATH, '//*[@id="center_column"]/form/p/button')
    CONTINUE_SHOPPING_BUTTON_IN_ADDRESS_TAB = (By.XPATH, '//*[@id="center_column"]/form/p/a')
    PROCEED_TO_CHECKOUT_BUTTON_IN_SHIPPING_TAB = (By.XPATH, '//*[@id="form"]/p/button')
    CONTINUE_SHOPPING_BUTTON_IN_SHIPPING_TAB = (By.XPATH, '//*[@id="form"]/p/a')
    CONTINUE_SHOPPING_BUTTON_IN_PAYMENT_TAB = (By.XPATH, '//*[@id="center_column"]/div/p/a')
    PAY_BY_BANK_WIRE_BUTTON_IN_PAYMENT_TAB = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    PAY_BY_CHECK_BUTTON_IN_PAYMENT_TAB = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
    OTHER_PAYMENT_METHODS_BUTTON_IN_PAYMENT_TAB = (By.XPATH, '//*[@id="cart_navigation"]/a')
    CONFIRM_MY_ORDER_BUTTON_IN_PAYMENT_TAB = (By.XPATH, '//*[@id="cart_navigation"]/button')

    """Check-box"""
    AGREE_TERMS_SERVICE_CHECK_BOX_IN_SHIPPING_TAB = (By.XPATH, '//*[@id="cgv"]')  # Required field
