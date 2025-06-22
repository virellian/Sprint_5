import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#------------------------------------- вход по кнопке «Войти в аккаунт» на главной -------------------------------------

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://stellarburgers.nomoreparties.site/')
    current_url = driver.current_url
    time.sleep(1)

    # Переход на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
    time.sleep(1)

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("valeriakrasavina24241@yandex.ru")
    # Найди поле "Пароль" и заполни его (корректный пароль)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456")

    #Клик по кнопке Войти
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
    time.sleep(3)

    driver.quit()

main()