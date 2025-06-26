from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ------------------------------------- вход через кнопку «Личный кабинет» и выход из аккаунта---------------------------

class TestLogin:

    def test_login_from_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на кнопку «Личный кабинет»
        cabinet_button = (driver.find_element(By.XPATH,
                                              "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]"))
        cabinet_button.click()

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

        # Переход на кнопку «Личный кабинет»
        cabinet_button = (driver.find_element(By.XPATH,
                                              "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]"))
        cabinet_button.click()

        # Выход из аккаунта
        exit_butt = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and normalize-space(text())='Выход']")))
        exit_butt.click()

        # Локатор кнопки по классу
        order_button = (By.XPATH,
                        "//a[contains(@class, 'Auth_link__1fOlj')]")
        # Находим и проверяем
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(order_button))
        assert button.text.strip() == "Зарегистрироваться", f"Не найдена кнопка 'Зарегистрироваться'"


