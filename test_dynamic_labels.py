import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s
import tempfile
import pytest
from selenium import webdriver


# Фикстура для настройки браузера
@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    # Создание уникальной временной директории
    temp_dir = tempfile.mkdtemp(prefix='selenium_')

    # Инициализация опций драйвера
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={temp_dir}')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')

    # Установка опций в конфигурацию Selene
    browser.config.driver_options = options

    yield  # Здесь выполняется тест

    # Закрытие браузера после теста
    browser.quit()


@allure.feature("Issues в репозитории GitHub")
@allure.story("Поиск задач в чужом публичном репозитории")
@allure.severity(Severity.CRITICAL)
@allure.tag("web", "github", "search")
@allure.link("https://github.com/eroshenkoam/allure-example", name="Репозиторий examples")
def test_issues_find():
    # Динамические лейблы (альтернатива декораторам)
    allure.dynamic.feature("Issues в репозитории GitHub")
    allure.dynamic.story("Поиск задач в чужом публичном репозитории")

    # Открытие страницы GitHub
    browser.open("https://github.com")

    # Выполнение действий
    s(".header-search-button").click()
    s("input.FormControl-input.QueryBuilder-Input.FormControl-medium").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()

    # Проверка результатов
    s(by.partial_text("#")).should(be.visible)
