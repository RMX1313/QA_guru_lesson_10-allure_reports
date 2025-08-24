import allure
from allure_commons.types import Severity
from selene import browser, by
from selene.support.shared.jquery_style import s
import tempfile
import uuid
import pytest


# Фикстура для настройки браузера
@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    # Создание уникальной временной директории для пользовательских данных
    temp_dir = tempfile.mkdtemp(prefix='selenium_')

    # Настройка опций драйвера
    browser.config.driver_options.add_argument(f'--user-data-dir={temp_dir}')
    browser.config.driver_options.add_argument('--no-sandbox')
    browser.config.driver_options.add_argument('--disable-dev-shm-usage')
    browser.config.driver_options.add_argument('--headless')  # Для CI/CD

    yield  # Здесь выполняется тест

    # Закрытие браузера после теста
    browser.quit()


def test_issues_find():
    # Динамические лейблы Allure
    allure.dynamic.feature("Issues в репозитории GitHub")
    allure.dynamic.story("Поиск задач в чужом публичном репозитории")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.tag("web", "github", "search")
    allure.dynamic.link("https://github.com/eroshenkoam/allure-example", name="Репозиторий examples")

    # Открытие страницы GitHub
    browser.open("https://github.com")
    browser.driver.maximize_window()

    # Выполнение действий
    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()

    # Проверка результатов
    s(by.partial_text("#")).should(be.visible)


