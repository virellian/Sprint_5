import pytest
from selenium import webdriver


# ---------- Фикстура WebDriver ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
