from selenium.webdriver.common.by import By

class HomePageLocators:

    '''Хедер'''
    yandex_logo = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')  #  Логотип Яндекса
    scooter_logo = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')   #  Логотип Самоката
    header_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')  # Кнопка Заказать в хедере

    '''Остальные локаторы'''
    order_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')  # Кнопка Заказать в середтне страницы
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")


    '''Вопросы и ответы'''

    # Локаторы текста вопросов
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    # Локаторы текста ответов
    questions_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]

