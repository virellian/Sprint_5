import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures.driver import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures.driver import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ------------------------------------- вход по кнопке «Войти в аккаунт» на главной -------------------------------------


class TestLogin:
    def test_login_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # Ожидаем поле Email и вводим адрес
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='name']")))
        email_input.send_keys("valeriakrasavina24241@yandex.ru")

        # Ожидаем поле Пароль и вводим пароль
        password_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='Пароль']")))
        password_input.send_keys("123456")

        # Ожидаем кнопку "Войти" и кликаем
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]")))
        submit_button.click()

        # Ожидаем, что пользователь будет перенаправлен на главную (например, появится кнопка "Оформить заказ")
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

        driver.quit()
