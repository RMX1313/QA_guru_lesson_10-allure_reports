import allure
import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s


def test_issues_find():
    with allure.step("Открываем страницу"):
        browser.open("https://github.com/home")
        browser.driver.maximize_window()
    with allure.step("Поиск репозитория"):
        s(".header-search-button").click()
        s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
        s(by.link_text("eroshenkoam/allure-example-bamboo")).click()
    with allure.step("Находим issues"):
        s("#issues-tab").click()