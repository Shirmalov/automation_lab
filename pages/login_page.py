import allure
from config.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = Links.LOGIN_PAGE
        self.username_fld = ('xpath', '//input[@name="username"]')
        self.password_fld = ('xpath', '//input[@name="password"]')
        self.login_btn = ('xpath', '//button[@type="submit"]')

    @allure.step('Указать значение в поле "Username"')
    def fill_username_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.username_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Password"')
    def fill_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.password_fld)).send_keys(value)

    @allure.step('Нажать на кнопку "Login"')
    def click_on_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
