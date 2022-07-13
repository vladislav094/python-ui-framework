
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp

@pytest.mark.usefixtures("set_for_docker_without_ui")
class TestAuthorizationRegistrationNegative:
	def test_authorization_in_account_and_check_negative(self):
		automation_practice = AutomationpracticeApp(self.driver)
		sign_in = automation_practice.sign_in_page
		automation_practice.go_to("index.php?controller=authentication&back=my-account")
		sign_in.authorization_in_account()
		sign_in.assert_authentication_failed()

