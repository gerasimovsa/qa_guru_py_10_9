import allure
from selene import browser, be, by


@allure.step("Opening main page")
def open_main_page():
    browser.open("/")


@allure.step("Searching repository by name: {repo_name}")
def search_repo(repo_name):
    browser.element(".header-search-button").should(be.visible).click()
    browser.element("#query-builder-test").should(be.visible).click().type(repo_name).press_enter()


@allure.step("Opening repo with link text: {text}")
def click_on_repo_link(text):
    browser.element(by.link_text(text)).should(be.visible).click()


@allure.step("Opening issues tab")
def open_issues_tab():
    browser.element("#issues-tab").should(be.visible).click()


@allure.step("Validating that issue with {name} name is visible")
def check_issue_is_visible(name):
    browser.element(by.partial_text(name)).should(be.visible)
