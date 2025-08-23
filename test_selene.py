import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s


def test_issues_find():
    browser.open("https://github.com/home")
    browser.driver.maximize_window()
    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-example-bamboo")).click()
    s("#issues-tab").click()