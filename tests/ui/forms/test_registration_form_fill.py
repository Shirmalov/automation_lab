import allure
import pytest
from config.data import Data
from data.data_helper import data_helper
from data.forms.select_country import SelectCountry
from pages.forms.registration_form import RegistrationFormPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Простая форма регистрации')
@allure.title('AT-WSB0001: Тест на заполнение регистрационной формы')
def test_registration_form_fill(driver):
    username = data_helper.generate_username()
    email = data_helper.generate_email()
    registration_form_page = RegistrationFormPage(driver)
    registration_form_page.open()
    registration_form_page.click_on_forms_section_lnk()
    registration_form_page.check_name_form_section()
    registration_form_page.form_name_check()
    registration_form_page.fill_username_field(username)
    registration_form_page.fill_email_field(email)
    registration_form_page.fill_password_field(Data.PASSWORD)
    registration_form_page.select_country_ddl(SelectCountry.RU)
    registration_form_page.click_on_terms_of_use_chb()
    registration_form_page.click_on_register_button()
    registration_form_page.success_message_check()
