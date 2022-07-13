from selenium.webdriver.common.by import By


class AutomationPracticeMainPage:
    CART_WITH_ITEM_SHORT_FOR_ORDER = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img')
    CART_WITH_ITEM_BLOUSE_FOR_ORDER = (By.XPATH, "//img[@title='Blouse']")
    BTN_ADD_SHORT_ITEM_TO_CART = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]')
    BTN_ADD_BLOUSE_ITEM_TO_CART = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]')
    BTN_CONTINUE_SHOPPING = (By.XPATH, "//span[contains(@class,'continue btn')]//span[1]")
    BTN_SHOPPING_CART = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    SEARCH_FIELD = (By.XPATH, '//*[@id="search_query_top"]')
    BTN_SUBMIT_SEARCH = (By.XPATH, '//*[@id="searchbox"]/button')

    """Results of search"""
    PRODUCT_NAME_IN_RESULT_SEARCH = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')

