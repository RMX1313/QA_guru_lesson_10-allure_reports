import allure
from allure_commons.types import Severity
from selene import browser, by, be, have
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
    options.add_argument('--window-size=1920,1080')  # Добавляем размер окна

    # Установка опций в конфигурацию Selene
    browser.config.driver_options = options
    browser.config.timeout = 10  # Увеличиваем таймаут

    yield  # Здесь выполняется тест

    # Закрытие браузера после теста
    browser.quit()


@allure.feature("Issues в репозитории GitHub")
@allure.story("Поиск задач в чужом публичном репозитории")
@allure.severity(Severity.CRITICAL)
@allure.tag("web", "github", "search")
@allure.link("https://github.com/eroshenkoam/allure-example", name="Репозиторий examples")
def test_issues_find():
    # Открытие страницы GitHub
    browser.open("https://github.com")

    # Исправленные селекторы для GitHub
    # Вместо кнопки используем поле поиска напрямую
    s(".header-search-button").type("eroshenkoam/allure-example").press_enter()

    # Ищем репозиторий в результатах поиска
    s(by.link_text("eroshenkoam/allure-example")).click()

    # Переходим во вкладку Issues
    s("#issues-tab").click()

    # Проверяем, что есть хотя бы один issue
    s(by.partial_text("#")).should(be.visible)


# Альтернативный вариант с более надежными селекторами
def test_issues_find_alternative():
    browser.open("https://github.com/search")

    # Прямой поиск репозитория
    s("[name='q']").type("eroshenkoam/allure-example").press_enter()

    # Фильтруем по репозиториям
    s("[data-testid='results-filter']").click()
    s("[data-testid='search-filter-button-Repositories']").click()

    # Открываем нужный репозиторий
    s(by.link_text("eroshenkoam/allure-example")).click()

    # Issues tab
    s("[data-tab-item='issues-tab']").click()

    # Проверка
    s(".js-issue-row").should(be.visible)
