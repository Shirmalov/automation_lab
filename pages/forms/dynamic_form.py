import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class DynamicFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.form_name = ('xpath', '//h3[.="3. Динамическая форма"]')
        self.name_fld = ('xpath', '//input[@id="dyn-name"]')

        self.add_email_btn = ('xpath', '//button[@id="addEmailBtn"]')
        self.email_fld = ('xpath', '(//input[@name="email[]"])[1]')

        self.add_phone_btn = ('xpath', '//button[@id="addPhoneBtn"]')
        self.phone_fld = ('xpath', '(//input[@name="phone[]"])[1]')


        self.email_error = ('xpath', '//p[.="Email должен содержать символ @"]')
        self.val_password_fld = ('xpath', '//input[@id="val-password"]')
        self.password_error = ('xpath', '//p[.="Password должен содержать минимум 8 символов, включая буквы и цифры"]')
        self.val_confirm_password_fld = ('xpath', '//input[@id="val-confirm-password"]')
        self.confirm_password_error = ('xpath', '//p[.="Пароли не совпадают"]')
        self.submit_btn = ('xpath', '//button[@id="valSubmitBtn"]')
        self.success_message = ('xpath', '//p[normalize-space()="Все проверки пройдены! Форма валидна."]')
        self.failure_message = ('xpath',
                                '//p[normalize-space()="Форма содержит ошибки. Исправьте их и попробуйте снова."]')

    @allure.step('Скроллить до заголовка формы')
    def scroll_to_form_name(self):
        element = self.wait.until(EC.presence_of_element_located(self.form_name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Проверить название формы')
    def check_name_form(self):
        message = self.wait.until(EC.visibility_of_element_located(self.form_name))
        assert message.text.strip() == '2. Форма с валидацией', \
            f'Ожидалось "2. Форма с валидацией", но получено: "{message.text.strip()}"'

    @allure.step('Указать значение в поле "Username"')
    def fill_val_username_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.name_fld)).send_keys(value)

    @allure.step('Проверить ошибку в поле "Username"')
    def get_username_error(self) -> str | None:
        return self.get_error_text(self.username_error)

    @allure.step('Указать значение в поле "Email"')
    def fill_val_email_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_email_fld)).send_keys(value)

    @allure.step('Проверить ошибку в поле "Email"')
    def get_email_error(self) -> str | None:
        return self.get_error_text(self.email_error)

    @allure.step('Указать значение в поле "Password"')
    def fill_val_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_password_fld)).send_keys(value)

    @allure.step('Проверить ошибку в поле "Password"')
    def get_password_error(self) -> str | None:
        return self.get_error_text(self.password_error)

    @allure.step('Указать значение в поле "Подтвердите Password"')
    def fill_val_confirm_password_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.val_confirm_password_fld)).send_keys(value)

    @allure.step('Проверить ошибку в поле "Подтвердите Password"')
    def get_confirm_password_error(self) -> str | None:
        return self.get_error_text(self.confirm_password_error)

    @allure.step('Нажать на кнопку "Проверить и отправить"')
    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

    @allure.step('Проверить сообщение об успешной отправке формы')
    def check_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.success_message))
        assert message.text.strip() == 'Все проверки пройдены! Форма валидна.', \
            f'Ожидалось "Все проверки пройдены! Форма валидна.", но получено: "{message.text.strip()}"'

    @allure.step('Проверить сообщение об ошибке при отправке формы')
    def check_failure_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.failure_message))
        assert message.text.strip() == 'Форма содержит ошибки. Исправьте их и попробуйте снова.', \
            f'Ожидалось "Форма содержит ошибки. Исправьте их и попробуйте снова.", но получено: "{message.text.strip()}"'
