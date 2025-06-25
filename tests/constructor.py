import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures.driver import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ---------------------------------------------- раздел «Конструктор»----------------------------------------------------

class TestConstructor:
    def test_login_from_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на кнопку «конструктор»
        el_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'AppHeader_header__link_active')]")))
        time.sleep(1)
        el_input.click()

        # «Булки»
        tab_wrapper = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class, 'text_type_main-default') and text()='Булки']/ancestor::div[contains(@style, 'display: flex')]"
        )))
        tab_wrapper.click()

        heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h2[contains(@class, 'text_type_main-medium') and text()='Булки']"
            ))
        )

        is_visible = driver.execute_script(
            "const el = arguments[0];"
            "const rect = el.getBoundingClientRect();"
            "return (rect.top >= 0 && rect.bottom <= window.innerHeight);",
            heading
        )

        assert is_visible, "'Булки' не видны на экране"

        # «Соусы»
        tab_wrapper = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class, 'text_type_main-default') and text()='Соусы']/ancestor::div[contains(@style, 'display: flex')]"
        )))
        tab_wrapper.click()

        heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h2[contains(@class, 'text_type_main-medium') and text()='Соусы']"
            ))
        )

        is_visible = driver.execute_script(
            "const el = arguments[0];"
            "const rect = el.getBoundingClientRect();"
            "return (rect.top >= 0 && rect.bottom <= window.innerHeight);",
            heading
        )

        assert is_visible, "'Соусы' не видны на экране"

        # «Начинки»
        tab_wrapper = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class, 'text_type_main-default') and text()='Начинки']/ancestor::div[contains(@style, 'display: flex')]"
        )))
        tab_wrapper.click()

        heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h2[contains(@class, 'text_type_main-medium') and text()='Начинки']"
            ))
        )

        is_visible = driver.execute_script(
            "const el = arguments[0];"
            "const rect = el.getBoundingClientRect();"
            "return (rect.top >= 0 && rect.bottom <= window.innerHeight);",
            heading
        )

        assert is_visible, "'Начинки' не видны на экране"
