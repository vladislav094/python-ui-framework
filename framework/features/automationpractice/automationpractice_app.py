from framework.features.automationpractice.main_page import MainPage
# from framework.features.automationpractice.shopping_cart_page import
from framework.features.automationpractice.sing_in_page import SignInPage



class AutomationpracticeApp:
	def __init__(self, driver):
		self.driver = driver
		self.main_page = MainPage(self.driver)
		self.sign_in_page = SignInPage(self.driver)
		self.url = "http://automationpractice.com/"



	def go_to(self, resource):
		self.driver.get(self.url + resource)