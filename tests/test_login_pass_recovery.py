import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from url_config import UrlConfig
from locators import Locators


# ------------------------------------- вход через кнопку в форме восстановления пароля ---------------------------------

class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(UrlConfig.get_full_url())
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Ожидаем кнопку "Войти в аккаунт" и кликаем
        login_button = wait.until(
            EC.element_to_be_clickable(Locators.login_button_main))
        login_button.click()

        # Переход на кнопку "Забыли пароль? Восстановить пароль"
        driver.find_element(*Locators.restore_password_link).click()

        # Переход на кнопку "Вспомнили пароль? Войти"
        login_button = wait.until(
            EC.element_to_be_clickable(Locators.restore_login_link))
        login_button.click()

        # Ожидаем поле Email и вводим адрес
        email_input = wait.until(
            EC.presence_of_element_located(Locators.email_input))
        email_input.send_keys("valeriakrasavina24241@yandex.ru")

        # Ожидаем поле Пароль и вводим пароль
        password_input = wait.until(
            EC.presence_of_element_located(Locators.password_input))
        password_input.send_keys("123456")

        # Ожидаем кнопку "Войти" и кликаем
        submit_button = wait.until(EC.element_to_be_clickable(Locators.submit_button))
        submit_button.click()

        # Локатор кнопки по классу
        order_button = Locators.order_button
        # Находим и проверяем
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(order_button))
        assert button.text.strip() == "Оформить заказ", f"Не найдена кнопка 'Оформить заказ'"
