import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opt

# @pytest.fixture(scope="class")
@pytest.fixture
def get_chrome_options():
    options = chr_opt()
    # options.add_argument('--headless')
    options.add_argument("--start-maximized")
    return options

# @pytest.fixture(scope="class")
@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    # driver.set_window_rect(x=None, y=None, width=1920, height=1080)
    return driver

# @pytest.fixture(scope="class")
@pytest.fixture
def get_actions(get_webdriver):
    actions = webdriver.ActionChains(get_webdriver)
    return actions

# @pytest.fixture(scope="class")
@pytest.fixture
def set_up(request, get_webdriver):
    driver = get_webdriver
    url = "http://demo.guru99.com/test/newtours/register.php"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


# @pytest.fixture(scope="class")
@pytest.fixture
def set_to_hw_24(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
