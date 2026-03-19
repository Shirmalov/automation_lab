import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.links import Links


class BasePage:

    def __init__(self, driver):
        self.page_url = Links.WEB_PAGE
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

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

    def get_error_text(self, locator: tuple[str, str]) -> str | None:
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text.strip()
        except TimeoutException:
            return None
