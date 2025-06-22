import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#------------------------------------- вход через кнопку «Личный кабинет» и выход из аккаунта---------------------------

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://stellarburgers.nomoreparties.site/')
    current_url = driver.current_url
    time.sleep(1)

    # Переход на кнопку «Личный кабинет»
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
    time.sleep(1)

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("valeriakrasavina24241@yandex.ru")
    # Найди поле "Пароль" и заполни его (корректный пароль)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456")

    #Клик по кнопке Войти
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
    time.sleep(1)

    # Переход на кнопку «Личный кабинет»
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
    time.sleep(1)

    # Выход из аккаунта
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]").click()
    time.sleep(1)

    driver.quit()

main()