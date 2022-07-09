import pytest

from framework.features.heroku.herokuapp import HerokuApp


@pytest.mark.usefixtures("set_to_hw_24")
class TestSuite:
    def test_webpage_dynamic_controls(self):
        heroku = HerokuApp(self.driver)
        dynamic_page = heroku.dynamic_page
        heroku.go_to("dynamic_controls")
        dynamic_page.find_check_box()
        dynamic_page.find_btn_remove_and_click()
        dynamic_page.wait_text_1()
        dynamic_page.find_input_and_check_disabled()
        dynamic_page.click_btn_under_input()
        dynamic_page.wait_text_2()
        dynamic_page.find_input_and_check_enabled()


    def test_webpage_iframe(self):
        heroku = HerokuApp(self.driver)
        frame = heroku.frames_page
        heroku.go_to("frames")
        frame.find_link_and_click()
        frame.find_frame_and_switch()
        frame.compare_text_in_frame()
