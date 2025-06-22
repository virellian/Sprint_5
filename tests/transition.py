import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#-------------------------- переход из личного кабинета в конструктор  и на логотип Stellar Burgers --------------------

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://stellarburgers.nomoreparties.site/')
    current_url = driver.current_url
    time.sleep(1)

    # Переход на кнопку «Личный кабинет»
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
    time.sleep(1)

    # Переход из Личного кабинета в логотип
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div").click()
    time.sleep(1)

    # Переход из логотипа в конструктор
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a").click()
    time.sleep(1)

    driver.quit()

main()
