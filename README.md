# Финальный проект 6 спринта курса "Автоматизатор тестирования на Python", "Page Object"

## Описание проекта

В этом проекте написаны автотесты для учебного сервиса «Яндекс.Самокат». Его разработали специально для студентов.

## Файлы

- allure_results - каталог с отчетом о тестировании

- data/data.py - данные для тестов

- locators/home_page_locators.py -  локаторы домашней страницы
- locators/order_page_locators.py -  локаторы страницы заказа

- pages/base_page.py  -  файл с базовыми методами взаимодействия с элементами
- pages/home_page.py  -  файл с методами домашней страницы
- pages/order_page.py  -  файл с методами страницы заказа

- tests/test_header_links.py -  файл с проверками работы логотипов в хедере
- tests/test_home_page.py  -  файл с проверками ответов на вопросы
- tests/test_order_page.py  -  файл с проверками регистрации, двумя путями

- conftest.py  -  файл с фикстурами
- requirements.txt  -  файл с внешними зависимостями

## Запуск

- Установить зависимости  -  pip install -r requirements.txt
- Запустить тесты  -  pytest --alluredir=allure_results
- Вывести отчёты Allure  -  allure serve allure_results