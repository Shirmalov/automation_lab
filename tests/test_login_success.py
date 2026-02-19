import time
import pytest
import allure
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и завершения работы браузера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver

    driver.quit()


@allure.epic("Тестирование Swag Labs")
@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
@allure.title("TITLE-SW0001: Успешная авторизация на сайте Orange HRM")
@pytest.mark.smoke
@pytest.mark.regress
def test_login_success(driver):
    """Проверяет успешную авторизацию стандартного пользователя."""

    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.open().login("Admin", "admin123")

    # Assert
    login_page.verify_login_success()
    time.sleep(5)


# # Все тесты
# pytest tests/ -v
#
# # Только smoke
# pytest tests/ -v -m smoke
#
# # С отчётом Allure
# pytest tests/ -v --alluredir=allure-results
# allure serve allure-results

