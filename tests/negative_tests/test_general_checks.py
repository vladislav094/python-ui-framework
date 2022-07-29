import allure
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp

@pytest.mark.usefixtures("set_up_webdriver")
class TestGeneralChecks:
	@allure.description("In that test we try assert wrong title main page")
	@allure.severity(severity_level="MINOR")
	def test_check_wrong_title_of_the_page(self):
		automation_practice = AutomationpracticeApp(self.driver)
		main_page = automation_practice.main_page
		automation_practice.go_to("index.php")
		main_page.check_title_main_page_wrong()






