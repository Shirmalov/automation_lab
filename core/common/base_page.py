import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from typing import Optional, Union


class BasePage:
    """Базовый класс для всех страниц. Реализует паттерн Page Object."""

    def __init__(self, driver: WebDriver, url: Optional[str] = None):
        self.driver = driver
        self.url = url
        self.timeout = 10

    @allure.step("Открыть страницу")
    def open(self) -> "BasePage":
        """Открывает URL страницы."""
        if self.url:
            self.driver.get(self.url)
        return self

    @allure.step("Проверить URL страницы")
    def wait_for_url(self, expected_url: str, timeout: Optional[int] = None) -> bool:
        """Ожидает, что текущий URL совпадёт с ожидаемым."""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.url_to_be(expected_url)
            )
            return True
        except TimeoutException:
            raise AssertionError(
                f"Ожидаемый URL: {expected_url}\n"
                f"Фактический URL: {self.driver.current_url}"
            )

    @allure.step("Проверить, что URL содержит текст")
    def wait_for_url_contains(self, text: str, timeout: Optional[int] = None) -> bool:
        """Ожидает, что текущий URL содержит указанный текст."""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            raise AssertionError(
                f"URL не содержит ожидаемый текст: '{text}'\n"
                f"Фактический URL: {self.driver.current_url}"
            )

    @allure.step("Найти элемент")
    def find_element(self, by: By, value: str, timeout: Optional[int] = None):
        """Находит элемент с явным ожиданием."""
        wait_time = timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((by, value))
        )

    @allure.step("Найти видимый элемент")
    def find_visible_element(self, by: By, value: str, timeout: Optional[int] = None):
        """Находит видимый элемент с явным ожиданием."""
        wait_time = timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((by, value))
        )

    @allure.step("Кликнуть по элементу")
    def click(self, by: By, value: str, timeout: Optional[int] = None) -> "BasePage":
        """Находит элемент и кликает по нему."""
        element = self.find_visible_element(by, value, timeout)
        element.click()
        return self

    @allure.step("Ввести текст в поле")
    def fill_field(self, by: By, value: str, text: str, timeout: Optional[int] = None) -> "BasePage":
        """Находит поле и вводит в него текст."""
        element = self.find_visible_element(by, value, timeout)
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Получить текст элемента")
    def get_text(self, by: By, value: str, timeout: Optional[int] = None) -> str:
        """Находит элемент и возвращает его текст."""
        element = self.find_visible_element(by, value, timeout)
        return element.text

    @allure.step("Обновить страницу")
    def refresh(self) -> "BasePage":
        """Обновляет текущую страницу."""
        self.driver.refresh()
        return self

    @allure.step("Перейти назад")
    def go_back(self) -> "BasePage":
        """Переходит на предыдущую страницу в истории браузера."""
        self.driver.back()
        return self

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """Возвращает текущий URL."""
        return self.driver.current_url
