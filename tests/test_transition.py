from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from url_config import UrlConfig
from locators import Locators


# -------------------------- переход из личного кабинета в конструктор  и на логотип Stellar Burgers --------------------

class TestLogin:

    def test_login_from_account(self, driver):
        driver.get(UrlConfig.get_full_url())
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на кнопку «Личный кабинет»
        cabinet_button = driver.find_element(*Locators.cabinet_button)
        cabinet_button.click()

        # Переход из Личного кабинета в логотип
        driver.find_element(*Locators.logo_link).click()

        # Переход из логотипа в конструктор
        driver.find_element(*Locators.constructor_link).click()

        assert UrlConfig.base_url in driver.current_url
