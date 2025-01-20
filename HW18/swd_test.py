import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_text():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Шаг 1: Перейти на страницу логина
        driver.get("https://omayo.blogspot.com/")

        #Шаг 2: Найти поле с именем textbox1 и соседнее с ним
        text_field1 = driver.find_element(By.ID, "textbox1")


        #Шаг 3: Очистить поле с id textbox1
        text_field1.clear()

        #Шаг 4: Ввести текст в поле textbox1 и кликом по соседнему полю сохранить введеное значение
        text_field1.send_keys("Selenium.Test")

        #Шаг 5. Проверить что в поле у нас сохранилось наше значение
        my_text = "Selenium.Test"
        assert text_field1.get_attribute('value') == my_text, f"Ожидался ранее введенный текст, но что то пошло не так"

    finally:
        # Закрытие браузера
        driver.quit()

def test_select():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:

        # Шаг 1: Перейти на страницу логина
        driver.get("https://omayo.blogspot.com/")

        #Шаг 2 Ищем наше поле с селектом
        select_field = driver.find_element(By.ID, "drop1")
        select_field.click()

        #Шаг 3 Выбираем опцию док3
        dok3 = driver.find_element(By.ID, "ironman4")
        dok3.click()

        #Шаг 4. Проверяем что у нас выбрана именно doc3
        assert dok3.is_displayed()

        # import pdb
        # pdb.set_trace()


    finally:
        # Закрытие браузера
        driver.quit()