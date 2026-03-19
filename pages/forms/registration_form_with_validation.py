import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class RegistrationFormWithValidationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.forms_section = ('xpath', '//div[.="Формы"]')
        self.form_name = ('xpath', '//h3[.="2. Форма с валидацией"]')
        self.val_username_fld = ('xpath', '//input[@id="val-username"]')
        self.val_email_fld = ('xpath', '//input[@id="val-email"]')
        self.val_password_fld = ('xpath', '//input[@id="val-password"]')
        self.val_confirm_password_fld = ('xpath', '//input[@id="val-confirm-password"]')
        self.val_register_btn = ('xpath', '//button[@id="valSubmitBtn"]')
        self.success_message = ('xpath', '//p[normalize-space()="Все проверки пройдены! Форма валидна."]')

    @allure.step('Открыть раздел "Формы и Inputs"')
    def click_on_forms_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.forms_section)).click()

    @allure.step('Скроллить до заголовка формы')
    def scroll_to_form_name(self):
        element = self.wait.until(EC.presence_of_element_located(self.form_name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Проверить название формы')
    def form_name_check(self):
        message = self.wait.until(EC.visibility_of_element_located(self.form_name))
        assert message.text.strip() == '2. Форма с валидацией', \
            f'Ожидалось "2. Форма с валидацией", но получено: "{message.text.strip()}"'

    @allure.step('Указать значение в поле "Username"')
    def fill_val_username_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_username_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Email"')
    def fill_val_email_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_email_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Password"')
    def fill_val_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_password_fld)).send_keys(value)

    @allure.step('Указать значение в поле "Подтвердите Password"')
    def fill_val_confirm_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_confirm_password_fld)).send_keys(value)

    @allure.step('Нажать на кнопку "Проверить и отправить"')
    def click_on_val_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.val_register_btn)).click()

    @allure.step('Проверить сообщение об успешной отправке формы')
    def success_message_check(self):
        message = self.wait.until(EC.visibility_of_element_located(self.success_message))
        assert message.text.strip() == 'Все проверки пройдены! Форма валидна.', \
            f'Ожидалось "Все проверки пройдены! Форма валидна.", но получено: "{message.text.strip()}"'
