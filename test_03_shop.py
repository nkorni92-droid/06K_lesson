from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    wait = WebDriverWait(driver, 10)
    
    # Открываем сайт
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    
    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    
    # Нажимаем Continue
    driver.find_element(By.ID, "continue").click()
    
    # Читаем итоговую стоимость
    total = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    
    print(f"Итоговая стоимость: {total}")
    
    # Проверяем, что сумма = $58.29
    assert "$58.29" in total, \
        f"Ожидалась сумма $58.29, получено '{total}'"
    
    print("✅ Сумма заказа верна!")