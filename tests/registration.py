from selenium.webdriver.common.by import By
from text_generator import text_generator

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ------------------------------------- Регистрация ------------------------------------------------------------
class TestLogin:

    def test_login_from_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на регистрацию
        cabinet_button = (driver.find_element(By.XPATH,
                                              "//a[contains(@class, 'Auth_link__1fOlj') and normalize-space(text())='Зарегистрироваться']"))
        cabinet_button.click()

        # ---Успешная регистрация---

        # Найди поле "Имя" и заполни его
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Имя']]//input")))
        email_input.send_keys(text_generator(False))

        # Ожидаем поле Email и вводим адрес
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Email']]//input")))
        email_input.send_keys(f"{text_generator(False)}@yandex.ru")

        # Найди поле "Пароль" и заполни его (некорректный пароль)
        pswd_input = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Пароль']]//input")))
        pswd_input.send_keys(text_generator(True))

        # Клик по кнопке Зарегистрироваться
        cabinet_button = (driver.find_element(By.XPATH,
                                              "//button[contains(@class, 'button_button__33qZ0')]"))
        cabinet_button.click()

        assert driver.find_elements(By.XPATH,
                                    "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//*[normalize-space(text())='Некорректный пароль']")

        # очистка поля пароля
        pswd_input.click()
        pswd_input.clear()

        # Найди поле "Пароль" и заполни его (корректный пароль)
        pswd_input.send_keys("123456")

        # Клик по кнопке Зарегистрироваться
        cabinet_button.click()

        # Находим и проверяем
        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert 'https://stellarburgers.nomoreparties.site' in driver.current_url
