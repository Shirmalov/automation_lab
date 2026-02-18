import allure
from selenium.webdriver.common.by import By
from core.common.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации Saucedemo."""

    URL = "https://www.saucedemo.com"

    # Локаторы
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_TITLE = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver, url: str = URL):
        super().__init__(driver, url)

    @allure.step("Открыть страницу логина")
    def open(self) -> "LoginPage":
        super().open()
        return self

    @allure.step("Ввести логин")
    def fill_username(self, username: str) -> "LoginPage":
        self.fill_field(*self.USERNAME_FIELD, username)
        return self

    @allure.step("Ввести пароль")
    def fill_password(self, password: str) -> "LoginPage":
        self.fill_field(*self.PASSWORD_FIELD, password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> "LoginPage":
        self.click(*self.LOGIN_BUTTON)
        return self

    @allure.step("Выполнить авторизацию")
    def login(self, username: str, password: str) -> "LoginPage":
        """Полный сценарий входа."""
        return (self
                .fill_username(username)
                .fill_password(password)
                .click_login())

    @allure.step("Проверить успешный вход")
    def verify_login_success(self) -> "LoginPage":
        """Проверяет, что пользователь успешно авторизован."""
        self.wait_for_url_contains("inventory.html")
        assert self.get_text(*self.INVENTORY_TITLE) == "Products"
        return self

    @allure.step("Получить текст ошибки")
    def get_error_message(self) -> str:
        """Возвращает текст сообщения об ошибке."""
        return self.get_text(*self.ERROR_MESSAGE)
