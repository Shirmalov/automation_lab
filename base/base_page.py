import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.admin_section = ('xpath', '//span[.="Admin"]')
        self.pim_section = ('xpath', '//span[.="PIM"]')
        self.leave_section = ('xpath', '//span[.="Leave"]')
        self.time_section = ('xpath', '//span[.="Time"]')

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

    @allure.step('Открыть раздел "Admin"')
    def click_on_admin_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_section)).click()

    @allure.step('Открыть раздел "PIM"')
    def click_on_pim_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_section)).click()

    @allure.step('Открыть раздел "Leave"')
    def click_on_leave_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.leave_section)).click()

    @allure.step('Открыть раздел "Time"')
    def click_on_time_section_lnk(self):
        self.wait.until(EC.element_to_be_clickable(self.time_section)).click()
