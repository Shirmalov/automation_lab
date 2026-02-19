import allure
from selenium.webdriver.common.by import By
from core.common.base_page import BasePage
from core.common.links import Links
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    """Страница авторизации Orange HRM."""

    URL = Links.LOGIN_URL

    USERNAME_FIELD = ('css_selector', 'input[name="username"]')
    PASSWORD_FIELD = ('css_selector', 'input[name="password"]')
    LOGIN_BUTTON = ('css_selector', 'button[type="submit"]')

    def __init__(self, driver, url: str = URL):
        super().__init__(driver, url)

    @allure.step('Открыть страницу логина')
    def open(self) -> "LoginPage":
        super().open()
        return self

    @allure.step('Ввести логин')
    def fill_login_field(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step('Ввести пароль')
    def fill_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password()


    @allure.step('Нажать кнопку "Login"')
    def click_on_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
