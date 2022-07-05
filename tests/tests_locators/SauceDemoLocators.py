import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from framework.webpage import WebPage
from loguru import logger


logger.add("debug.log", format="{time} {level} {message}",
		   level="DEBUG", rotation="100 KB")
# logger.debug('Error')
# logger.info('Information message')
# # logger.warning('Warning')

@pytest.mark.usefixtures('set_up')
class TestCase:
	def test_page(self):
		elt = WebPage(self.driver)
		data_login = "standard_user"
		data_password = "secret_sauce"
		input_username_field = elt.find_elt("xpath", "//input[@class='input_error form_input']").send_keys(data_login)
		input_password_field = elt.find_elt("xpath", "(//input[@class='input_error form_input'])[2]").send_keys(data_password)
		submit_button = elt.find_elt("xpath", "//input[@class='submit-button btn_action']").click()
		all_item = elt.find_elt("xpath", "//*[@class='inventory_list']/div")
		# print(elt.get_nav_links_text(all_item))


	def test_log_item(self):
		elt = WebPage(self.driver)
		for index in range(1, 7):
			items = elt.find_elts("xpath", f"//*[@class='inventory_list']/div[{index}]")
			print(elt.get_nav_links_text(items), index)
			logger.info(f"Information message: {elt.get_nav_links_text(items)} {index}")

		# data_login = elt.find_elt("xpath", "//*[@id='login_credentials']/text()[1]")

		# data_password = elt.find_elt("xpath", "//div[@class='login_password']/text()[1]")

		#
		# '''Page with items'''
		# burger_menu = elt.find_elt("xpath", "//div[@class='bm-burger-button']//button[1]")
		#
		# first_link_burger_menu = elt.find_elt("xpath", "//a[@class='bm-item menu-item']")
		# second_link_burger_menu = elt.find_elt("xpath", "(//a[@class='bm-item menu-item'])[2]")
		# third_link_burger_menu = elt.find_elt("xpath", "(//a[@class='bm-item menu-item'])[3]")
		# fourth_link_burger_menu = elt.find_elt("xpath", "(//a[@href='#'])[3]")
		# close_burger_menu = elt.find_elt("xpath", "//div[@class='bm-cross-button']//button[1]")


# def log_function(xpath):
