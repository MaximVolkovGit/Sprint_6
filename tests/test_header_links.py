from pages.home_page import HomePage
import time
from data.data import Urls
import allure

class TestHeaderLinks:


    @allure.title('Проверка перехода на страницу Дзена по клику на лого Яндекса в хедере')
    @allure.description('''1.Открываем главную страницу
                        2. Кликаем по лого Яндекса
                        3. Проверяем, что открылась страница Дзена по URL''')
    def test_yandex_logo_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_yandex_logo()
        home_page.go_to_new_tab()
        time.sleep(3)
        current_url = home_page.get_current_url()
        assert current_url == Urls.DZEN_PAGE

    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката в хедере')
    @allure.description('''1. Открываем главную страницу
                        2. Кликаем по кнопке Заказать для перехода на страницу заказа
                        3. Кликаем по лого Самоката
                        3. Проверяем, что открылась главная страница''')
    def test_scooter_logo_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_header_order_button()
        home_page.click_scooter_logo()
        assert home_page.get_current_url() == Urls.MAIN_PAGE

