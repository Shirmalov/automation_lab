import allure

from config.links import Links
from base.base_page import BasePage
from data.user_role import UserRole
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = Links.LOGIN_PAGE
        self.add_btn = ('xpath', '//button[.=" Add "]')
        self.search_btn = ('xpath', '//button[.=" Search "]')
        self.reset_btn = ('xpath', '//button[.=" Reset "]')
        self.username_fld = (
            'xpath', '//div[contains(@class, "oxd-input-group") and .//label[text()="Username"]]//input')
        self.user_role_dropdown = ('xpath',
                                   '//label[.="User Role"]/ancestor::div[contains(@class, '
                                   '"oxd-input-group")]//div[@class="oxd-select-text-input"]')
        self.user_role_option = ('xpath', '//div[contains(@class, "oxd-select-option") and text()="{}"]')

    @allure.step('Нажать на кнопку "Add"')
    def click_on_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_btn)).click()

    @allure.step('Нажать на кнопку "Search"')
    def click_on_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.search_btn)).click()

    @allure.step('Нажать на кнопку "Reset"')
    def click_on_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(self.reset_btn)).click()

    @allure.step('Указать значение в поле "Username"')
    def fill_username_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.username_fld)).send_keys(value)

    @allure.step('Выбор роли из поля "User Role"')
    def select_user_role(self, role: UserRole):
        self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        option = (By.XPATH, self.user_role_option[1].format(role))
        self.wait.until(EC.element_to_be_clickable(option)).click()
