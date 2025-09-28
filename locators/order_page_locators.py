from selenium.webdriver.common.by import By

class OrderPageLocators:


    '''Первая страница заказа'''
    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')  #  Поле ввода Имени
    family_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')  #  Поле ввода Фамилии
    adress_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  #  Поле ввода Адреса
    metro_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')  #  Поле ввода Станция метро
    metro_station = (By.XPATH, '//div[text() = "Черкизовская"]')  #  Станция в списке
    # metro_station = (By.XPATH, '//div[contains(text(), "Черкизовская")]/parent::button')   #  Станция в списке
    tel_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле ввода телефона

    next_button = (By.XPATH, '//button[text()="Далее"]') # Кнопка Далее

    '''Вторая страница заказа'''
    data_order_field = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле Когда привезти самокат
    rent_period_field = (By.XPATH, ".//span[@class='Dropdown-arrow']") #  Поле Срок аренды
    rent_period_one_day = (By.XPATH, ".//div[text() = 'сутки']")  #  Локатор для одних суток
    black_scooter_check = (By.ID, 'black')  #  Чек-бокс чёрного цвета
    gray_scooter_check = (By.ID, 'grey')  #  Чек-бокс серого цвета
    comment_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']") # Поле Комментарий для курьера
    back_button = (By.XPATH, ".//button[text() = 'Назад']")  # Кнопка Назад
    final_order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")  #  Кнопка Заказать в конце заказа

    '''Окно Хотите оформить заказ?'''
    no_button = (By.XPATH, ".//button[text() = 'Нет']")  # Кнопка Нет
    yes_button = (By.XPATH, ".//button[text() = 'Да']")  #  Кнопка Да

    '''Окно Заказ оформлен'''
    order_placed_text = (By.XPATH, ".//div[text() = 'Заказ оформлен']")  #  Заголовок окна
    view_status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")  #  Кнопка Посмотреть статус

    '''Окно заказа'''
    order_placed_text = (By.XPATH, ".//div[text() = 'Заказ оформлен']")  # Заголовок Заказ оформлен
    view_status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")  # Кнопка Посмотреть статус