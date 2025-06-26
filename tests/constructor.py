import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ---------------------------------------------- раздел «Конструктор»----------------------------------------------------

class TestConstructor:
    def test_check_sauce(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Нажали на раздел "Соусы"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Соусы')]"))
        ).click()

        # Проверяем наличие активного раздела
        WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"))
        ).is_displayed()

        # Ищем активную вкладку "Соусы" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Соусы')]")
            )
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Соусы' не найдена"

    def test_check_bread(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))
        ).click()

        # Нажали на раздел "Булки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Булки')]"))
        ).click()

        # Ищем активную вкладку "Булки" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Булки')]")
            )
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Булки' не найдена"

    def test_check_toppings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))
        ).click()

        # Ищем активную вкладку "Начинки" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Начинки')]")
            )
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Начинки' не найдена"
