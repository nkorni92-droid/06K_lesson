from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 50)  # Ждем до 50 секунд
    
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Вводим задержку 45 секунд
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажимаем кнопки: 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    # Ждем появления результата 15 (до 50 секунд)
    result = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    
    # Проверяем, что результат = 15
    screen = driver.find_element(By.CLASS_NAME, "screen")
    assert screen.text == "15", f"Ожидался результат 15, получен '{screen.text}'"
    
    print("✅ Калькулятор посчитал правильно!")