import time

import allure
import pytest
from data.data_helper import data_helper
from pages.forms.dynamic_form import DynamicFormPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Динамическая форма')
@allure.title('AT-WSB0004: Тест на заполнение динамической формы')
def test_registration_dynamic_form(driver):
    username = data_helper.generate_username()
    emails = [
        data_helper.generate_email(),
        data_helper.generate_email(),
        data_helper.generate_email(),
    ]

    dynamic_form_page = DynamicFormPage(driver)
    dynamic_form_page.open()
    dynamic_form_page.open_forms_section()
    dynamic_form_page.check_name_forms_section()
    dynamic_form_page.scroll_to_form_title()
    dynamic_form_page.check_form_title()

    dynamic_form_page.fill_dyn_name_field(username)

    dynamic_form_page.click_add_email()
    dynamic_form_page.click_add_email()
    assert dynamic_form_page.get_email_fields_count() == 3, \
        'Ожидалось 3 поля email после двух нажатий на "Добавить email"'

    for i, email in enumerate(emails):
        dynamic_form_page.fill_dyn_email_field(i, email)

    dynamic_form_page.click_on_delete_email_button(index=2)
    assert dynamic_form_page.get_email_fields_count() == 2, \
        'Ожидалось 2 поля email после удаления одного'

    dynamic_form_page.click_on_add_phone_button()
    assert dynamic_form_page.get_phone_fields_count() == 2, \
        'Ожидалось 2 поля телефон после нажатия на "Добавить телефон"'

    phones = [
        data_helper.generate_random_phone(),
        data_helper.generate_random_phone(),
    ]
    for i, phone in enumerate(phones):
        dynamic_form_page.fill_phone_field(i, phone)

    time.sleep(3)

    dynamic_form_page.click_on_delete_phone_button(index=1)
    assert dynamic_form_page.get_phone_fields_count() == 1, \
        'Ожидалось 1 поле телефон после удаления одного'

    time.sleep(5)