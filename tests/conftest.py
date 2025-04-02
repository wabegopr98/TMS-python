import pytest
import psycopg2
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DB_PARAMS = {
    'dbname': os.environ.get('POSTGRES_DB', 'taskmanager'),
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'host': os.environ.get('POSTGRES_HOST', 'localhost'), #localhost - запуск локальный, запустили додокер, db - д
    'port': os.environ.get('POSTGRES_PORT', '5432')
}




@pytest.fixture(scope="function")
def db_connection():
    """Фикстура для подключения к БД"""
    print("🔌 Подключение к БД...")
    conn = psycopg2.connect(**DB_PARAMS)  # Устанавливаем соединение с БД
    yield conn  # Передаем соединение в тест
    cur = conn.cursor()
    sql_delete = 'DELETE FROM task'
    cur.execute(sql_delete)
    sql_delete = 'DELETE FROM "user"'
    cur.execute(sql_delete)
    # Фиксируем изменения
    conn.commit()

    # Узнаем, сколько строк было удалено
    rows_deleted = cur.rowcount
    print(f"Удалено строк: {rows_deleted}")
    conn.close()  # Закрываем соединение после теста
    print("🔌 Соединение с БД закрыто.")




@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()
