import time

import pytest
from selenium.webdriver.support.ui import Select

from framework.webpage import WebPage


@pytest.mark.usefixtures("set_up")
class TestSuite:
    def test_webpage(self):
        elt = WebPage(self.driver)
        first_name = elt.find_elt("xpath", "//input[@name='firstName']")
        first_name.send_keys("Ivan")
        last_name = elt.find_elt("xpath", "//input[@name='lastName']")
        last_name.send_keys("Ivanov")
        phone = elt.find_elt("xpath", "//input[@name='phone']")
        phone.send_keys("+7 (999) 111 22 33")
        email = elt.find_elt("xpath", "//input[@id='userName']")
        email.send_keys("ivanov@ivan.ii")
        address = elt.find_elt("xpath", "//input[@name='address1']")
        address.send_keys("Lenin Avenue house 10 apartment 11")
        city = elt.find_elt("xpath", "//input[@name='city']")
        city.send_keys("Minsk")
        state = elt.find_elt("xpath", "//input[@name='state']")
        state.send_keys("Minsk")
        postal_code = elt.find_elt("xpath", "//input[@name='postalCode']")
        postal_code.send_keys("220056")
        country_drop = Select(elt.find_elt("xpath", "//select[@name='country']"))
        country_drop.select_by_value("BELARUS")
        user_name = elt.find_elt("xpath", "//input[@id='email']")
        user_name.send_keys("NewUser")
        password = elt.find_elt("xpath", "//input[@name='password']")
        password.send_keys("123456789")
        confirm_password = elt.find_elt("xpath", "//input[@name='confirmPassword']")
        confirm_password.send_keys("123456789")
        assert first_name.get_property("value") == "Ivan"
        assert last_name.get_property("value") == "Ivanov"
        assert user_name.get_property("value") == "NewUser"
        submit_ntn = elt.find_elt("xpath", "//input[@type='submit']")
        submit_ntn.click()
        time.sleep(30)
