from selenium.webdriver.common.by import By
from text_generator import text_generator

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from url_config import UrlConfig
from locators import Locators


# ------------------------------------- Регистрация ------------------------------------------------------------
class TestLogin:

    def test_login_from_account(self, driver):
        driver.get(UrlConfig.get_full_url('login'))
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на регистрацию
        cabinet_button = driver.find_element(*Locators.register_link)
        cabinet_button.click()

        # ---Успешная регистрация---

        # Найди поле "Имя" и заполни его
        email_input = wait.until(
            EC.presence_of_element_located(Locators.register_name_input))
        email_input.send_keys(text_generator(False))

        # Ожидаем поле Email и вводим адрес
        email_input = wait.until(
            EC.presence_of_element_located(Locators.register_email_input))
        email_input.send_keys(f"{text_generator(False)}@yandex.ru")

        # Найди поле "Пароль" и заполни его (некорректный пароль)
        pswd_input = wait.until(
            EC.presence_of_element_located(Locators.register_password_input))
        pswd_input.send_keys(text_generator(True))

        # Клик по кнопке Зарегистрироваться
        cabinet_button = driver.find_element(*Locators.register_button)
        cabinet_button.click()

        assert driver.find_elements(*Locators.register_error)

        # очистка поля пароля
        pswd_input.click()
        pswd_input.clear()

        # Найди поле "Пароль" и заполни его (корректный пароль)
        pswd_input.send_keys("123456")

        # Клик по кнопке Зарегистрироваться
        cabinet_button.click()

        # Находим и проверяем
        WebDriverWait(driver, 10).until(EC.url_to_be(UrlConfig.get_full_url('login')))

        assert UrlConfig.base_url in driver.current_url
