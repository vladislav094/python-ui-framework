import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opt


@pytest.fixture
def get_chrome_options_without_ui():
    options = chr_opt()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_webdriver_without_ui(get_chrome_options_without_ui):
    options = get_chrome_options_without_ui
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    return driver



@pytest.fixture
def get_actions_without_ui(get_webdriver_without_ui):
    actions = webdriver.ActionChains(get_webdriver_without_ui)
    return actions



@pytest.fixture
def set_for_docker_without_ui(request, get_webdriver_without_ui):
    driver = get_webdriver_without_ui
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()





@pytest.fixture
def get_chrome_options_with_ui():
    options = chr_opt()
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_webdriver_with_ui(get_chrome_options_with_ui):
    options = get_chrome_options_with_ui
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    return driver


@pytest.fixture
def set_with_ui(request, get_webdriver_with_ui):
    driver = get_webdriver_with_ui
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()



