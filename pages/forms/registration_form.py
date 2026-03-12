import allure

from config.links import Links
from base.base_page import BasePage
from data.forms.select_country import SelectCountry
from selenium.webdriver.support.ui import Select as SeleniumSelect
from selenium.webdriver.support import expected_conditions as EC


class RegistrationFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = Links.WEB_PAGE
        self.forms_section = ('xpath', '//div[.="Формы"]')
        self.username_fld = ('xpath', '//input[@id="username"]')
        self.email_fld = ('xpath', '//input[@id="email"]')
        self.password_fld = ('xpath', '//input[@id="password"]')
        self.country_ddl = ('xpath', '//select[@id="country"]')
        self.terms_of_use_chb = ('xpath', '//input[@id="terms"]')
        self.register_btn = ('xpath', '//button[@id="submitBtn"]')

    @allure.step('Открыть раздел "Формы и Inputs"')
    def click_on_forms_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.forms_section)).click()

    @allure.step('Указать значение в поле "Username"')
    def fill_username_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.username_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Email"')
    def fill_email_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.email_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Password"')
    def fill_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.password_fld)).send_keys(value)

    @allure.step('Выбрать страну в поле "Country"')
    def select_country_ddl(self, country: SelectCountry):
        select_element = self.wait.until(EC.presence_of_element_located(self.country_ddl))
        dropdown = SeleniumSelect(select_element)
        dropdown.select_by_visible_text(country.value)

    @allure.step('Активировать/Деактивировать чек-бокс "I agree to the Terms and Conditions"')
    def click_on_terms_of_use_chb(self):
        self.wait.until(EC.element_to_be_clickable(self.terms_of_use_chb)).click()

    @allure.step('Нажать на кнопку "Register"')
    def click_on_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.register_btn)).click()
