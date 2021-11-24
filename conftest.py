from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose your browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose your language')


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')
    language_name = request.config.getoption('language')

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language_name})
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(
            'Choose your browser between Chrome and Firefox')
    yield driver
    driver.quit()
