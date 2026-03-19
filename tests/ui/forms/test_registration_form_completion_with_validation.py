import time
import allure
import pytest
from config.data import Data
from data.data_helper import data_helper
from pages.forms.registration_form_with_validation import RegistrationFormWithValidationPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Форма с валидацией')
@allure.title('AT-WSB0002: Тест на заполнение регистрационной формы с валидацией')
def test_registration_form_completion_with_validation(driver):
    username = data_helper.generate_username()
    email = data_helper.generate_email()
    registration_page_with_val = RegistrationFormWithValidationPage(driver)
    registration_page_with_val.open()
    registration_page_with_val.click_on_forms_section_lnk()
    registration_page_with_val.scroll_to_form_name()
    registration_page_with_val.form_name_check()
    registration_page_with_val.fill_val_username_field(username)
    registration_page_with_val.fill_val_email_field(email)
    registration_page_with_val.fill_val_password_field(Data.PASSWORD)
    registration_page_with_val.fill_val_confirm_password_field(Data.PASSWORD)
    registration_page_with_val.click_on_val_register_button()
    registration_page_with_val.success_message_check()
    time.sleep(2)
