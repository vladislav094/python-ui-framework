
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp

@pytest.mark.usefixtures("set_up_webdriver")
class TestModuleSearch:
	def test_search_one_item(self):
		automation_practice = AutomationpracticeApp(self.driver)
		main_page = automation_practice.main_page
		automation_practice.go_to("index.php")
		main_page.fill_search_field_and_assert_result()