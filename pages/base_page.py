
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    '''Получить текущий URL'''
    def get_current_url(self):
        return self.driver.current_url
    

    @allure.step('Явное ожидание отображения локатора')
    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть по кнопке')
    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()


    @allure.step('Заполнение формы')
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    @allure.step('Скролл к нужному элементу')
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переход на новую вкладку браузера')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Видимость элемента')
    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()