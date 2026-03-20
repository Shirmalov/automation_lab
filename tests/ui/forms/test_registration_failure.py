import allure
import pytest
from pages.forms.form_with_validation import FormWithValidationPage


@pytest.mark.negative
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Форма с валидацией')
@allure.title('AT-WSB0003: Тест на заполнение регистрационной формы с ошибкой в валидации')
def test_registration_failure(driver):
    registration_validation_page = FormWithValidationPage(driver)
    registration_validation_page.open()
    registration_validation_page.open_forms_section()
    registration_validation_page.check_name_forms_section()
    registration_validation_page.scroll_to_form_name()
    registration_validation_page.check_name_form()

    test_data = {
        'username': {
            'value': 'name',
            'error': 'Username должен содержать минимум 5 символов',
            'check': registration_validation_page.get_username_error
        },
        'email': {
            'value': 'name.mail.com',
            'error': 'Email должен содержать символ @',
            'check': registration_validation_page.get_email_error
        },
        'password': {
            'value': '1aA!',
            'error': 'Password должен содержать минимум 8 символов, включая буквы и цифры',
            'check': registration_validation_page.get_password_error
        },
        'confirm_password': {
            'value': '2bB@',
            'error': 'Пароли не совпадают',
            'check': registration_validation_page.get_confirm_password_error
        }
    }

    registration_validation_page.fill_val_username_field(test_data['username']['value'])
    registration_validation_page.fill_val_email_field(test_data['email']['value'])
    registration_validation_page.fill_val_password_field(test_data['password']['value'])
    registration_validation_page.fill_val_confirm_password_field(test_data['confirm_password']['value'])
    registration_validation_page.click_on_submit_button()

    for field_name, config in test_data.items():
        with allure.step(f'Проверка ошибки для поля "{field_name}"'):
            error = config['check']()
            assert error is not None, f'[{field_name}] Ошибка не появилась!'
            assert config['error'] in error, f'[{field_name}] Ожидалось "{config["error"]}", но получено: "{error}"'

    registration_validation_page.check_failure_message()
