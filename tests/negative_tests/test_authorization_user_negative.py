
import pytest
from framework.features.automationpractice.automationpractice_app import AutomationpracticeApp
from framework.features.automationpractice.data.data_user_for_registration import DataUserForRegistration

@pytest.mark.usefixtures("set_up_webdriver")
class TestAuthorizationRegistrationNegative:
	def test_authorization_with_invalid_credentials_negative(self):
		automation_practice = AutomationpracticeApp(self.driver)
		sign_in = automation_practice.sign_in_page
		automation_practice.go_to("index.php?controller=authentication&back=my-account")
		sign_in.authorization_in_account()
		sign_in.assert_authentication_failed()



	@pytest.mark.parametrize('email', [
		DataUserForRegistration.EMAIL_ADDRESS_WITHOUT_DOMAIN,
		DataUserForRegistration.EMAIL_ADDRESS_WITHOUT_AT,
		DataUserForRegistration.EMAIL_ADDRESS_WITHOUT_DOT,
		DataUserForRegistration.EMAIL_ADDRESS_WITH_SPEC_CHARACTER
	])
	def test_registration_with_invalid_data_in_email_address_negative(self,email):
		automation_practice = AutomationpracticeApp(self.driver)
		sign_in = automation_practice.sign_in_page
		automation_practice.go_to("index.php?controller=authentication&back=my-account")
		sign_in.registration_with_invalid_email(email)
		sign_in.assert_invalid_email_address()


