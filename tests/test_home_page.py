import pytest
from pages.home_page import HomePage
from data.data import Questions
from locators.home_page_locators import HomePageLocators
import allure


class TestHomePage:
    
    @allure.title('Проверка текста ответов с параметризацией')
    @allure.description('''Параметризованный тест с поочерёдным открытием вопросов
                    и сверкой ответов с эталонными''')
    
    @pytest.mark.parametrize('question_number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_and_answers(self, driver, question_number):
        home_page = HomePage(driver)
        expected_answer = Questions.expected_question_text[question_number]
        
        home_page.scroll_to_question(question_number)
        home_page.click_question(question_number)
        actual_answer = home_page.get_answer_text(question_number)
        
        assert actual_answer == expected_answer, \
            f"Для вопроса {question_number} ожидался текст: '{expected_answer}', но получен: '{actual_answer}'"