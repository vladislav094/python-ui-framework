from selenium.webdriver.common.by import By


class FramesPageLocators:
    LINK_IFRAME = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
    IFRAME_WITH_DOCUMENT = (By.XPATH, '//*[@id="mce_0_ifr"]')
    TEXT = (By.XPATH, '//*[@id="tinymce"]/p')
