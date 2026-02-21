import time
import allure
import pytest
from config.data import Data
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic("Тестирование Orange HRM")
@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
@allure.title("AT-HRM0001: Успешная авторизация на сайте Orange HRM")
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_username_field(Data.LOGIN)
    login_page.fill_password_field(Data.PASSWORD)
    login_page.click_on_login_button()
    time.sleep(5)
