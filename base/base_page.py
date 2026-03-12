import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.forms_section = ('xpath', '//div[.="Формы"]')
        self.tables_section = ('xpath', '//div[.="Таблицы"]')
        self.modals_section = ('xpath', '//div[.="Модальные окна"]')
        self.drag_drop_section = ('xpath', '//div[.="Drag & Drop"]')

    def open(self):
        with allure.step(f'Open {self.page_url} page'):
            self.driver.get(self.page_url)

    def is_opened(self):
        with allure.step(f'Page {self.page_url} is opened'):
            self.wait.until(EC.url_to_be(self.page_url))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @allure.step('Открыть раздел "Формы и Inputs"')
    def click_on_forms_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.forms_section)).click()

    @allure.step('Открыть раздел "Таблицы"')
    def click_on_tables_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.tables_section)).click()

    @allure.step('Открыть раздел "Модальные окна"')
    def click_on_modals_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.modals_section)).click()

    @allure.step('Открыть раздел "Drag & Drop"')
    def click_on_drag_drop_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.drag_drop_section)).click()
