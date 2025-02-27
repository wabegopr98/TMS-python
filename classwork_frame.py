import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()

def test_window(driver):
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "tabButton").click()
    opened_handles = driver.window_handles
    driver.switch_to.window(opened_handles[1])
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page", \
        "Текст не соответствует"
    driver.close()
    driver.switch_to.window(opened_handles[0])
    assert driver.current_window_handle == opened_handles[0]

def test_task_frame(driver):
    driver.get("https://demoqa.com/frames")
    driver.switch_to.frame("frame1")
    my_elem = driver.find_element(By.ID, "sampleHeading").text
    assert my_elem == "This is a sample page"
    driver.switch_to.default_content()
    driver.switch_to.frame("frame2")
    my_elem2 = driver.find_element(By.ID, "sampleHeading").text
    assert my_elem2 == "This is a sample page"

def test_alert(driver):
    driver.get("https://demoqa.com/alerts")
    alert_button1 = driver.find_element(By.ID, "alertButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button1)
    alert_button1.click()
    my_al = driver.switch_to.alert
    assert my_al.text == "You clicked a button"
    my_al.accept()
    alert_button2 = driver.find_element(By.ID, "confirmButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button2)
    alert_button2.click()
    my_dism = driver.switch_to.alert
    assert my_dism.text == "Do you confirm action?"
    my_dism.dismiss()
    alert_button3 = driver.find_element(By.ID, "promtButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button3)
    alert_button3.click()
    my_prom = driver.switch_to.alert
    assert my_prom.text == "Please enter your name"
    my_prom.send_keys("Selenium Test")
    my_prom.accept()
    result = driver.find_element(By.ID, "promptResult")
    assert "Selenium Test" in result.text

def test_action(driver):
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
    env1 = driver.find_element(By.ID, "draggable")
    env2 = driver.find_element(By.ID, "droppable")
    action = ActionChains(driver)
    action.drag_and_drop(env1,env2).perform()
    if "Dropped" in env2.text:
        print("Перетаскивание выполнено успешно")
    driver.quit()
