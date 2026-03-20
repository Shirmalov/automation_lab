import time
import allure
import pytest
from pages.forms.registration_validation_form import RegistrationValidationPage


@pytest.mark.negative
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Форма с валидацией')
@allure.title('AT-WSB0002: Тест на заполнение регистрационной формы с ошибкой в валидации')
def test_failure_registration_form_completion_with_validation(driver):
    registration_page_with_val = RegistrationValidationPage(driver)
    registration_page_with_val.open()
    registration_page_with_val.click_on_forms_section_lnk()
    registration_page_with_val.scroll_to_form_name()
    registration_page_with_val.check_form_name()

    test_data = {
        'username': {
            'value': 'name',
            'error': 'Username должен содержать минимум 5 символов',
            'check': registration_page_with_val.get_username_error
        },
        'email': {
            'value': 'name.mail.com',
            'error': 'Email должен содержать символ @',
            'check': registration_page_with_val.get_email_error
        },
        'password': {
            'value': '1aA!',
            'error': 'Password должен содержать минимум 8 символов, включая буквы и цифры',
            'check': registration_page_with_val.get_password_error
        },
        'confirm_password': {
            'value': '2bB@',
            'error': 'Пароли не совпадают',
            'check': registration_page_with_val.get_confirm_password_error
        }
    }

    registration_page_with_val.fill_val_username_field(test_data['username']['value'])
    registration_page_with_val.fill_val_email_field(test_data['email']['value'])
    registration_page_with_val.fill_val_password_field(test_data['password']['value'])
    registration_page_with_val.fill_val_confirm_password_field(test_data['confirm_password']['value'])
    registration_page_with_val.click_on_val_register_button()

    for field_name, config in test_data.items():
        with allure.step(f'Проверка ошибки для поля "{field_name}"'):
            error = config['check']()
            assert error is not None, f'[{field_name}] Ошибка не появилась!'
            assert config['error'] in error, f'[{field_name}] Ожидалось "{config["error"]}", но получено: "{error}"'

    registration_page_with_val.failure_message_check()
    time.sleep(2)
