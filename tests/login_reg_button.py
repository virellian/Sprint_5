from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Ожидаем кнопку "Войти в аккаунт" и кликаем
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")))
        login_button.click()

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

        # Локатор кнопки по классу
        order_button = (By.XPATH,
                        "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')]")
        # Находим и проверяем
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(order_button))
        assert button.text.strip() == "Оформить заказ", f"Не найдена кнопка 'Оформить заказ'"
