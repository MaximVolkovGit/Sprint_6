from pages.home_page import HomePage
import time
from data.data import Urls
import allure

class TestHeaderLinks:


    @allure.title('Проверка перехода на страницу Дзена по клику на дого Яндекса в хедере')
    @allure.description('''1.Открываем главную страницу
                        2.кликаем по лого Яндекса
                        3. проверяем, что открылась страница Дзена по URL''')
    def test_yandex_logo_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_yandex_logo()
        home_page.go_to_new_tab()
        time.sleep(3)
        current_url = home_page.get_current_url()
        assert current_url == Urls.DZEN_PAGE