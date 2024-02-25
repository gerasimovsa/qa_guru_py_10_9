import allure
from allure_commons.types import Severity
from selene import browser, be, by
from tests.test_steps import *


@allure.suite("Github - Issues - Issue Name")
class TestGithubIssueName:
    def test_github_issue_selene_steps(self):
        allure.dynamic.title("Selene test")
        allure.dynamic.tag("Web Interface")
        allure.dynamic.severity(Severity.NORMAL)
        allure.dynamic.label("owner", "SergeyG")
        allure.dynamic.feature("Issues tab")
        allure.dynamic.story("Verify that issue of repository has name")
        allure.dynamic.link("https://github.com", name="Github main page")

        browser.open("/")
        browser.element(".header-search-button").should(be.visible).click()
        browser.element("#query-builder-test").should(be.visible).click().type(
            "eroshenkoam/allure-example").press_enter()
        browser.element(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()
        browser.element("#issues-tab").should(be.visible).click()
        browser.element(by.partial_text("69 nice")).should(be.visible)

    @allure.title("Lambda steps test")
    @allure.tag("Web Interface")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "SergeyG")
    @allure.feature("Issues tab")
    @allure.story("Verify that issue of repository has name")
    @allure.link("https://github.com", name="Github main page")
    def test_github_issue_lambda_steps(self):
        with allure.step("Opening main page"):
            browser.open("/")
        with allure.step("Clicking on search button"):
            browser.element(".header-search-button").should(be.visible).click()
        with allure.step("Entering repository name into search field and submitting"):
            browser.element("#query-builder-test").should(be.visible).click().type(
                "eroshenkoam/allure-example").press_enter()
        with allure.step("Clicking on repo link by text"):
            browser.element(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()
        with allure.step("Opening issues tab"):
            browser.element("#issues-tab").should(be.visible).click()
        with allure.step("Validating that issue with the given name is visible"):
            browser.element(by.partial_text("69 nice")).should(be.visible)

    @allure.title("Decorator steps test")
    @allure.tag("Web Interface")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "SergeyG")
    @allure.feature("Issues tab")
    @allure.story("Verify that issue of repository has name")
    @allure.link("https://github.com", name="Github main page")
    def test_github_issue_decorator_steps(self):
        open_main_page()
        search_repo("eroshenkoam/allure-example")
        click_on_repo_link("eroshenkoam/allure-example")
        open_issues_tab()
        check_issue_is_visible("69 nice")
