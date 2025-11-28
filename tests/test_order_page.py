from pages.order_page import OrderPage
from pages.home_page import HomePage
from data.data import Users
import allure


class TestOrderPage:

    @allure.title('Проверка оформления заказа по кнопке "Заказать" в хедере')
    @allure.description('Процедура заполнения форм заказа вынесена в отдельный метод')
    def test_order_by_click_on_header_button(self, driver):

        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_header_order_button()
        order_page.order_by_click_on_header_button(Users.user_1) # Заполнение формы заказа с данными user_1
        assert order_page.check_order_title()  #  Проверка появления окна Заказ оформлен

    @allure.title('Проверка оформления заказа по кнопке "Заказать" в середине домашней страницы')
    @allure.description('Процедура заполнения форм заказа вынесена в отдельный метод')  
    def test_order_by_click_on_main_button(self, driver):

        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_order_button()
        order_page.order_by_click_on_header_button(Users.user_2) # Заполнение формы заказа с данными user_2
        assert order_page.check_order_title()  #  Проверка появления окна Заказ оформлен
        

