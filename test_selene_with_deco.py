import allure
import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s


def test_steps_with_deco():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example-bamboo")
    open_issue_tab()


@allure.step("Открываем страницу")
def open_main_page():
    browser.open("https://github.com/home")
    browser.driver.maximize_window()


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-example-bamboo")).click()


@allure.step("Находим issues")
def open_issue_tab():
    s("#issues-tab").click()