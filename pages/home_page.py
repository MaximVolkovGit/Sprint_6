import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import time

class HomePage(BasePage):

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_button(HomePageLocators.header_order_button)

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_button(HomePageLocators.yandex_logo)
    
    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_button(HomePageLocators.scooter_logo)

    @allure.step('Скроллить к вопросу номер {question_number}')
    def scroll_to_question(self, question_number):
        question_locator = HomePageLocators.questions[question_number]
        self.scroll_to_locator(question_locator)
                
    @allure.step('Кликнуть на вопрос номер {question_number} и подождать, пока откроется ответ' )
    def click_question(self, question_number):
        question_locator = HomePageLocators.questions[question_number]
        self.click_button(question_locator)
        self.find_and_wait_locator(HomePageLocators.questions_text[question_number])
    
    @allure.step('Получить текст ответа на вопрос номер {question_number}')
    def get_answer_text(self, question_number):
        answer_locator = HomePageLocators.questions_text[question_number]
        return self.get_text_locator(answer_locator)
    
    @allure.step('Проверить вопрос-ответ номер {question_number}')
    def check_question_answer(self, question_number, expected_text):
        """Полный цикл проверки вопроса и ответа"""
        self.scroll_to_question(question_number)
        self.click_question(question_number)
        actual_text = self.get_answer_text(question_number)
        return actual_text == expected_text
    
    