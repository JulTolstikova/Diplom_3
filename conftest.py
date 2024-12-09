import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser! Please choose 'chrome' or 'firefox'.")

    driver.get(data.MAIN_URL)
    yield driver
    driver.quit()
