import allure
from allure_commons.types import Severity
from selene import browser, by
from selene.support.shared.jquery_style import s
import test_selene

def test_issues_find():
    # Динамические лейблы Allure
    allure.dynamic.feature("Issues в репозитории GitHub")
    allure.dynamic.story("Поиск задач в чужом публичном репозитории")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.tag("web", "github", "search")
    allure.dynamic.link("https://github.com/eroshenkoam/allure-example", name="Репозиторий examples")


    browser.open("https://github.com/home")
    browser.driver.maximize_window()
    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-example-bamboo")).click()
    s("#issues-tab").click()