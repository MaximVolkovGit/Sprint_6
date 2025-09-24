import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageHeaderLocators

class HomePage(BasePage):

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.find_element(HomePageHeaderLocators.header_order_button).click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.find_element(HomePageHeaderLocators.yandex_logo).click()
    
    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self):
        self.find_element(HomePageHeaderLocators.scooter_logo).click()