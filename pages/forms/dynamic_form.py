import allure

from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DynamicFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.form_name = ('xpath', '//h3[.="3. Динамическая форма"]')
        self.dyn_name_fld = ('id', 'dyn-name')
        self.add_email_btn = ('id', 'addEmailBtn')
        self.dyn_email_fld = ('xpath', '//input[@name="email[]"]')
        self.delete_email_btn = ('xpath', '//button[@onclick="removeEmailField(this)"]')
        self.add_phone_btn = ('id', 'addPhoneBtn')
        self.dyn_phone_fld = ('name', 'phone[]')
        self.delete_phone_btn = ('xpath', '//button[@onclick="removePhoneField(this)"]')
        self.submit_btn = ('xpath', '//button[@id="dynSubmitBtn"]')
        self.result_message = ('id', 'dynFormResult')
        self.result_name = ('xpath', '//*[@id="dynFormResult"]//p[strong[contains(., "Имя")]]')
        self.result_email = ('xpath', '//*[@id="dynFormResult"]//p[strong[contains(., "Email")]]')
        self.result_phone = ('xpath', '//*[@id="dynFormResult"]//p[strong[contains(., "Телефон")]]')


    def _get_nth(self, locator: tuple, index: int):
        """Возвращает n-й элемент из группы по локатору (index с 0)."""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))[index]

    @allure.step('Скроллить до заголовка формы')
    def scroll_to_form_title(self):
        element = self.wait.until(EC.presence_of_element_located(self.form_name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Проверить название формы')
    def check_form_title(self):
        element = self.wait.until(EC.visibility_of_element_located(self.form_name))
        expected = '3. Динамическая форма'
        assert element.text.strip() == expected, \
            f'Ожидалось "{expected}", получено: "{element.text.strip()}"'

    @allure.step('Заполнить поле "Ваше имя"')
    def fill_dyn_name_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.dyn_name_fld)).send_keys(value)

    @allure.step('Нажать кнопку "Добавить email"')
    def click_on_add_email_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_email_btn)).click()

    @allure.step('Заполнить поле email №{index}')
    def fill_dyn_email_field(self, index: int, value: str):
        self._get_nth(self.dyn_email_fld, index).send_keys(value)

    @allure.step('Удалить поле email №{index}')
    def click_on_delete_email_button(self, index: int):
        self._get_nth(self.delete_email_btn, index).click()

    @allure.step('Добавить и заполнить email поля')
    def add_and_fill_emails(self, emails: list[str]):
        for i, email in enumerate(emails):
            if i > 0:
                self.click_on_add_email_button()
            self.fill_dyn_email_field(i, email)

    def get_email_fields_count(self) -> int:
        return len(self.driver.find_elements(*self.dyn_email_fld))

    @allure.step('Нажать кнопку "Добавить телефон"')
    def click_on_add_phone_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_phone_btn)).click()

    @allure.step('Заполнить поле телефон №{index}')
    def fill_phone_field(self, index: int, value: str):
        self._get_nth(self.dyn_phone_fld, index).send_keys(value)

    @allure.step('Удалить поле телефон №{index}')
    def click_on_delete_phone_button(self, index: int):
        self._get_nth(self.delete_phone_btn, index).click()

    def get_phone_fields_count(self) -> int:
        return len(self.driver.find_elements(*self.dyn_phone_fld))

    @allure.step('Нажать на кнопку "Отправить форму"')
    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

    @allure.step('Проверить сообщение об успешной отправке формы')
    def check_result_message(self):
        self.wait.until(EC.visibility_of_element_located(self.result_message))

    @allure.step('Проверить имя в результате')
    def check_result_name(self, expected_name: str):
        element = self.wait.until(EC.visibility_of_element_located(self.result_name))
        actual = element.text.replace('Имя:', '').strip()
        assert actual == expected_name, \
            f'Имя: ожидалось "{expected_name}", получено "{actual}"'

    @allure.step('Проверить email адреса в результате')
    def check_result_emails(self, expected_emails: list[str]):
        element = self.wait.until(EC.visibility_of_element_located(self.result_email))
        actual_text = element.text.split(':', 1)[-1].strip()
        actual = [e.strip() for e in actual_text.split(',')]
        assert actual == expected_emails, \
            f'Email: ожидалось "{expected_emails}", получено "{actual}"'

    @allure.step('Проверить телефоны в результате')
    def check_result_phones(self, expected_phones: list[str]):
        element = self.wait.until(EC.visibility_of_element_located(self.result_phone))
        actual_text = element.text.split(':', 1)[-1].strip()
        actual = [p.strip() for p in actual_text.split(',')]
        assert actual == expected_phones, \
            f'Телефоны: ожидалось "{expected_phones}", получено "{actual}"'
