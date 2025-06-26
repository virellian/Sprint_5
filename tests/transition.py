from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# -------------------------- переход из личного кабинета в конструктор  и на логотип Stellar Burgers --------------------

class TestLogin:

    def test_login_from_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

        # Переход на кнопку «Личный кабинет»
        cabinet_button = (driver.find_element(By.XPATH,
                                              "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]"))
        cabinet_button.click()

        # Переход из Личного кабинета в логотип
        driver.find_element(By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']/a").click()

        # Переход из логотипа в конструктор
        driver.find_element(By.XPATH,
                            "//*[contains(@class, 'AppHeader_header__link__3D_hX') and contains(@class, 'AppHeader_header__link_active__1IkJo')]").click()

        assert 'https://stellarburgers.nomoreparties.site' in driver.current_url
