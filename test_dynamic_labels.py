import allure
from allure_commons.types import Severity
from selene import browser, by
from selene.support.shared.jquery_style import s


def test_issues_find():
    # Настройка браузера с уникальной директорией пользовательских данных
    browser.config.driver_options.add_argument('--user-data-dir=/tmp/selenium_user_data')
    browser.config.driver_options.add_argument('--no-sandbox')
    browser.config.driver_options.add_argument('--disable-dev-shm-usage')

    # Динамические лейблы Allure
    allure.dynamic.feature("Issues в репозитории GitHub")
    allure.dynamic.story("Поиск задач в чужом публичном репозитории")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.tag("web", "github", "search")
    allure.dynamic.link("https://github.com/eroshenkoam/allure-example", name="Репозиторий examples")

    browser.open("https://github.com")
    browser.driver.maximize_window()

    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()

    # Закрытие браузера после теста
    browser.quit()
