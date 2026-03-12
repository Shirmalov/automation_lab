import time
import allure
import pytest
from data.forms.select_country import SelectCountry
from pages.forms.registration_form import RegistrationFormPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.epic('Тестирование WEB Sandbox')
@allure.feature('Формы')
@allure.story('Простая форма регистрации')
@allure.title('AT-WSB0001: Тест на заполнение регистрационной формы')
def test_registration_form_completion(driver):
    registration_page = RegistrationFormPage(driver)
    registration_page.open()
    registration_page.click_on_forms_section_lnk()
    registration_page.fill_username_field("test_user")
    registration_page.fill_email_field("test@example.com")
    registration_page.fill_password_field("secure_pass")
    registration_page.select_country_ddl(SelectCountry.RU)
    registration_page.click_on_terms_of_use_chb()
    registration_page.click_on_register_button()
    time.sleep(5)
