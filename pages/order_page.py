from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def send_name_to_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.name_field, text)

    @allure.step('Заполнить поле Фамилия')
    def send_last_name_to_last_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.family_field, text)

    @allure.step('Заполнить поле Адрес')
    def send_address_to_address_field(self, text):
        self.send_keys_to_field(OrderPageLocators.adress_field, text)

    @allure.step('Заполнить поле Станция метро')
    def send_metro_station_to_metro_station_field(self, text):
        self.click_button(OrderPageLocators.metro_field)
        self.send_keys_to_field(OrderPageLocators.metro_field, text)
        self.click_button(OrderPageLocators.metro_station)

    @allure.step('Заполнить поле Телефон')
    def send_telephon_number(self, text):
        self.send_keys_to_field(OrderPageLocators.tel_field, text)

    @allure.step('Клик по кнопке Далее')
    def click_next_button(self):
        self.click_button(OrderPageLocators.next_button)
    
    @allure.step('Заполнить поле Когда привезти самокат')
    def send_when_deliver_scooter(self, text):
        self.click_button(OrderPageLocators.data_order_field)
        self.send_keys_to_field(OrderPageLocators.data_order_field, text)

    @allure.step('Заполнить поле Срок аренды')
    def send_rental_period_field(self):
        self.click_button(OrderPageLocators.rent_period_field)
        self.click_button(OrderPageLocators.rent_period_one_day)

    @allure.step('Выбрать чёрный цвет самоката')
    def choose_black_scooter(self):
        self.click_button(OrderPageLocators.black_scooter_check)

    @allure.step('Выбрать серый цвет самоката')
    def choose_gray_scooter(self):
        self.click_button(OrderPageLocators.gray_scooter_check)

    @allure.step('Заполнить поле Комментарий для курьера')
    def send_comment_for_the_courier(self, text):
        self.send_keys_to_field(OrderPageLocators.comment_field, text)

    @allure.step('Клик по кнопке Заказать в конце заказа')
    def click_final_order_button(self):
        self.click_button(OrderPageLocators.final_order_button)

    @allure.step('Клик по кнопке Да в окне Хотите оформить заказ?')
    def confirm_the_order(self):
        self.click_button(OrderPageLocators.yes_button)
    
    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.order_placed_text).is_displayed()

    @allure.step('Заполнение всей формы заказа')
    def order_by_click_on_header_button(self, user):
        self.send_name_to_name_field(user[1])            # Заполнить Имя
        self.send_last_name_to_last_name_field(user[2])  # Заполнить фамилиию
        self.send_address_to_address_field(user[3])      # Заполнить адрес
        self.send_metro_station_to_metro_station_field(user[4])  # Заполнить станцию метро
        self.send_telephon_number(user[5])               #  Заполнить телефон
        self.click_next_button()                               # Нажать Далее
        self.send_when_deliver_scooter(user[6])          # Указать время доставки
        self.send_rental_period_field()                        # Указать период аренды
        self.choose_black_scooter()                            # Выбрать чёрный скутер
        self.send_comment_for_the_courier(user[7])       # Оставить коммент
        self.click_final_order_button()                        # Нажать Заказать
        self.confirm_the_order()                               # Подтвердить заказ
        