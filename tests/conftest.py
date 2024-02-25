import pytest
from selene import browser
import allure


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    with allure.step("Setting up base page url"):
        browser.config.base_url = "https://github.com"
    with allure.step("Selecting Firefox for browser"):
        browser.config.driver_name = "firefox"
    with allure.step("Setting up timeout for browser"):
        browser.config.timeout = 8
    with allure.step("Setting up browser window size"):
        browser.config.window_width = 1200
        browser.config.window_height = 720
    yield
    browser.quit()
