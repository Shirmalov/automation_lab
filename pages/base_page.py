import allure
from retrying import retry
from selene.api import browser, have, s
from selene.core.exeptions import TimeoutExeption
from selenium.common import JavascriptExeption
from selenium.webdriver import Keys
from waiting import TimeoutExpired, wait



class BasePage:
    def __init__(self):
        pass


    @staticmethod
    @allure.step('')
    def assure_current_page_url(expected_url: str, timeout: int = 5):
        try:
            browser.with_(timeout=timeout).should(have.url(expected_url))
        except TimeoutExeption as e:
            raise AssertionError(f'Не удалось перейти на страницу: \n{e}')