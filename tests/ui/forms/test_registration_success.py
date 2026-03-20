import allure
import pytest
from config.data import Data
from data.data_helper import data_helper
from pages.forms.registration_validation_form import RegistrationValidationPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Форма с валидацией')
@allure.title('AT-WSB0002: Тест на заполнение регистрационной формы с успешной валидацией')
def test_registration_success(driver):
    username = data_helper.generate_username()
    email = data_helper.generate_email()
    registration_validation_page = RegistrationValidationPage(driver)
    registration_validation_page.open()
    registration_validation_page.click_on_forms_section_lnk()
    registration_validation_page.check_name_form_section()
    registration_validation_page.scroll_to_form_name()
    registration_validation_page.check_form_name()
    registration_validation_page.fill_val_username_field(username)
    registration_validation_page.fill_val_email_field(email)
    registration_validation_page.fill_val_password_field(Data.PASSWORD)
    registration_validation_page.fill_val_confirm_password_field(Data.PASSWORD)
    registration_validation_page.click_on_val_register_button()
    registration_validation_page.success_message_check()
