from selenium.webdriver.common.by import By


class DynamicControlsPageLocators:
    FIRST_CHECKBOX = (By.XPATH, "//div[@id='checkbox']//input[1]")
    INPUT_FIELD = (By.XPATH, "//*[@id='input-example']/input")
    BTN_REMOVE = (By.XPATH, "//*[@id='checkbox-example']/button")
    BTN_UNDER_INPUT = (By.XPATH, "//*[@id='input-example']/button")
    TEXT = (By.XPATH, "//*[@id='message']")
