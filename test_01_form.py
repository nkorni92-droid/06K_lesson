from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    # Используем Edge или Safari по заданию
    driver = webdriver.Edge()  # или webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submit(driver):
    wait = WebDriverWait(driver, 10)
    
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    # Нажимаем Submit
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    
    # Ждем, что поле Zip code стало красным
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class"), \
        "Поле Zip code должно быть красным!"
    
    # Проверяем, что остальные поля зеленые
    green_fields = ["first-name", "last-name", "address", "e-mail", 
                    "phone", "city", "country", "job-position", "company"]
    
    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, \
            f"Поле {field_id} должно быть зеленым!"
    
    print("✅ Все проверки пройдены!")