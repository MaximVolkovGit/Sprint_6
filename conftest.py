
import pytest
from selenium import webdriver

from data.data import Urls


# @allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


