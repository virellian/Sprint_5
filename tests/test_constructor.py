import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from url_config import UrlConfig
from locators import Locators

# ---------------------------------------------- раздел «Конструктор»----------------------------------------------------

class TestConstructor:
    def test_check_sauce(self, driver):
        driver.get(UrlConfig.get_full_url())

        # Нажали на раздел "Соусы"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.sauce_tab)
        ).click()

        # Проверяем наличие активного раздела
        WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located(Locators.active_tab)
        ).is_displayed()

        # Ищем активную вкладку "Соусы" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.active_tab_sauce)
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Соусы' не найдена"

    def test_check_bread(self, driver):
        driver.get(UrlConfig.get_full_url())

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.toppings_tab)
        ).click()

        # Нажали на раздел "Булки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.bread_tab)
        ).click()

        # Ищем активную вкладку "Булки" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.active_tab_bread)
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Булки' не найдена"

    def test_check_toppings(self, driver):
        driver.get(UrlConfig.get_full_url())

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.toppings_tab)
        ).click()

        # Ищем активную вкладку "Начинки" (по классу и тексту)
        active_tab = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(Locators.active_tab_toppings)
        )
        assert active_tab.text.strip(), "Ошибка: активная вкладка 'Начинки' не найдена"
