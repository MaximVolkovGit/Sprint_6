import pytest
import time
from pages.home_page import HomePage
from data.urls import Urls


class TestHomePage:
    
    def test_yandex_logo_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_yandex_logo()
        home_page.go_to_new_tab()
        time.sleep(5)
        current_url = home_page.get_current_url()
        assert current_url == Urls.DZEN_PAGE


