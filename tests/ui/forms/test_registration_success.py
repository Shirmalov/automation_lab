import allure
import pytest
from config.data import Data
from data.data_helper import data_helper
from pages.forms.form_with_validation import FormWithValidationPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Форма с валидацией')
@allure.title('AT-WSB0002: Тест на заполнение регистрационной формы с успешной валидацией')
def test_registration_success(driver):
    username = data_helper.generate_username()
    email = data_helper.generate_email()
    registration_validation_page = FormWithValidationPage(driver)
    registration_validation_page.open()
    registration_validation_page.open_forms_section()
    registration_validation_page.check_name_forms_section()
    registration_validation_page.scroll_to_form_name()
    registration_validation_page.check_name_form()
    registration_validation_page.fill_val_username_field(username)
    registration_validation_page.fill_val_email_field(email)
    registration_validation_page.fill_val_password_field(Data.PASSWORD)
    registration_validation_page.fill_val_confirm_password_field(Data.PASSWORD)
    registration_validation_page.click_on_submit_button()
    registration_validation_page.check_success_message()
