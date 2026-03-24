import allure

from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DynamicFormPage(BasePage):
    FORM_TITLE = (By.XPATH, '//h3[.="3. Динамическая форма"]')
    DYN_NAME_FIELD = (By.ID, 'dyn-name')
    ADD_EMAIL_BTN = (By.ID, 'addEmailBtn')
    EMAIL_FIELDS = (By.XPATH, '//input[@name="email[]"]')
    DELETE_EMAIL_BTNS = (By.XPATH, '//button[@onclick="removeEmailField(this)"]')
    ADD_PHONE_BTN = (By.ID, 'addPhoneBtn')
    PHONE_FIELDS = (By.NAME, 'phone[]')
    DELETE_PHONE_BTNS = (By.XPATH, '//button[@onclick="removePhoneField(this)"]')

    def _get_nth(self, locator: tuple, index: int):
        """Возвращает n-й элемент из группы по локатору (index с 0)."""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))[index]

    @allure.step('Скроллить до заголовка формы')
    def scroll_to_form_title(self):
        element = self.wait.until(EC.presence_of_element_located(self.FORM_TITLE))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Проверить название формы')
    def check_form_title(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FORM_TITLE))
        expected = '3. Динамическая форма'
        assert element.text.strip() == expected, \
            f'Ожидалось "{expected}", получено: "{element.text.strip()}"'

    @allure.step('Заполнить поле "Ваше имя"')
    def fill_name_field(self, value: str):
        self.wait.until(EC.element_to_be_clickable(self.DYN_NAME_FIELD)).send_keys(value)

    @allure.step('Нажать кнопку "Добавить email"')
    def click_add_email(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_EMAIL_BTN)).click()

    @allure.step('Заполнить поле email №{index}')
    def fill_email_field(self, index: int, value: str):
        self._get_nth(self.EMAIL_FIELDS, index).send_keys(value)

    @allure.step('Удалить поле email №{index}')
    def click_delete_email(self, index: int):
        self._get_nth(self.DELETE_EMAIL_BTNS, index).click()

    @allure.step('Добавить и заполнить email поля')
    def add_and_fill_emails(self, emails: list[str]):
        for i, email in enumerate(emails):
            if i > 0:
                self.click_add_email()
            self.fill_email_field(i, email)

    def get_email_fields_count(self) -> int:
        return len(self.driver.find_elements(*self.EMAIL_FIELDS))

    @allure.step('Нажать кнопку "Добавить телефон"')
    def click_add_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PHONE_BTN)).click()

    @allure.step('Заполнить поле телефон №{index}')
    def fill_phone_field(self, index: int, value: str):
        self._get_nth(self.PHONE_FIELDS, index).send_keys(value)

    @allure.step('Удалить поле телефон №{index}')
    def click_delete_phone(self, index: int):
        self._get_nth(self.DELETE_PHONE_BTNS, index).click()

    def get_phone_fields_count(self) -> int:
        return len(self.driver.find_elements(*self.PHONE_FIELDS))
