
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp

@pytest.mark.usefixtures("set_up_webdriver")
class TestRegistrationAuthorization:
	def test_registration_new_user(self):
		automation_practice = AutomationpracticeApp(self.driver)
		sign_in = automation_practice.sign_in_page
		automation_practice.go_to("index.php?controller=authentication&back=my-account")
		sign_in.registration_new_account()
		sign_in.fill_block_with_personal_information_for_required_fields()
		sign_in.scroll_page_to_block_your_address()
		sign_in.fill_block_with_address_for_required_fields()
		sign_in.click_button_for_register_new_account()
		sign_in.assert_my_name_in_personal_account()

	def test_authorization_in_account_and_check(self):
		automation_practice = AutomationpracticeApp(self.driver)
		sign_in = automation_practice.sign_in_page
		automation_practice.go_to("index.php?controller=authentication&back=my-account")
		sign_in.authorization_in_account()
		sign_in.assert_my_name_in_personal_account()