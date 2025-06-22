import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

# ------------------------------------- Регистрация ------------------------------------------------------------
def text_generator(pswd=False):
    chars = string.ascii_letters + string.digits
    if pswd == True:
        chars += "!@#$%^&*()_+-="
    password = ''.join(random.choices(chars, k=8))
    return password


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://stellarburgers.nomoreparties.site/login')
    current_url = driver.current_url
    time.sleep(1)

    # Переход на регистрацию
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
    time.sleep(1)

    # ---Успешная регистрация---

    # Найди поле "Имя" и заполни его
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        text_generator(False))
    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(
        f"{text_generator(False)}yandex.ru")
    # Найди поле "Пароль" и заполни его (некорректный пароль)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(text_generator(True))

    # Клик по кнопке Зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    time.sleep(1)

    # если ошибка "пользователь уже существует"
    if driver.find_element(By.XPATH, "/html/body/div/div/main/div/p"):
        # Ищем блок текста "пользователь уже существует" и проверяем его
        error_element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/p")
        assert "Такой пользователь уже существует" in error_element.text  # Проверяем текст

    elif driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p"):
        # Ищем блок текста "Некорректный пароль" и проверяем его
        error_element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")
        assert "Некорректный пароль" in error_element.text  # Проверяем текст

    # очистка поля пароля
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").clear()
    # Найди поле "Пароль" и заполни его (корректный пароль)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")

    # Клик по кнопке Зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    time.sleep(2)

    driver.quit()


main()
