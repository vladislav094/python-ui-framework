
import pytest
from selenium import webdriver
from framework.common.env_vars import should_run_headless




@pytest.fixture
def _get_chrome_options() -> webdriver.ChromeOptions:

        """
        Creates a set of options for running the Chrome browser.
        Runs Chrome in headless mode depending on the value of the RUN_HEADLESS environment variable.
        :return: A set of options to run the Chrome browser with.
        """

        chrome_options = webdriver.ChromeOptions()
        run_headless = should_run_headless()

        if run_headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-setuid-sandbox")

        return chrome_options


@pytest.fixture
def get_webdriver(_get_chrome_options):
    options = _get_chrome_options
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver


@pytest.fixture
def set_up_webdriver(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def get_actions(get_webdriver):
    actions = webdriver.ActionChains(get_webdriver)
    return actions



