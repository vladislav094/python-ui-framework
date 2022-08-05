
import pytest
from selenium import webdriver
from framework.common.env_vars import should_run_headless



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.100.7")
    parser.addoption("--bversion", action="store", default="")

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
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--ignore-certificate-errors")

        return chrome_options


@pytest.fixture
def get_webdriver(_get_chrome_options, request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")

    # executor_url = f"http://{executor}:4444/wd/hub"
    executor_url = f"https://selenium2-1.dev-bitrix.by/wd/hub/"
    # executor_url = f"https://192.168.100.20:4444/wd/hub/"

    capabilities = {
        "browserName" : browser,
        "browserVersion" : version,
        "selenoid:options": {
            "enableVNC" : True
            # "enableVideo": False
        }
    }
    options = _get_chrome_options
    # driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(command_executor=f'http://{executor}:4444/wd/hub', options=options)
    driver = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor=executor_url)
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



