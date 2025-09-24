import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageHeaderLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перейти на новую вкладку браузера')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])