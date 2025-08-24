import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Добавляем уникальный user-data-dir для каждого запуска
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_profile")

    browser.config.driver_options = chrome_options
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 15.0

    yield

    browser.quit()
