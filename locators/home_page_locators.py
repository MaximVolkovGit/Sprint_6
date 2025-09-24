from selenium.webdriver.common.by import By

class HomePageHeaderLocators:

    """Хедер"""
    yandex_logo = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    scooter_logo = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    header_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')