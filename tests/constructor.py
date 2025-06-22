import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#---------------------------------------------- раздел «Конструктор»----------------------------------------------------

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://stellarburgers.nomoreparties.site/')
    current_url = driver.current_url
    time.sleep(1)

    # Переход на кнопку «конструктор»
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a").click()
    time.sleep(2)

    #«Булки»
    error_element1 = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[1]")
    assert "Булки" in error_element1.text

    #«Соусы»
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]").click()
    error_element1 = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]")
    assert "Соусы" in error_element1.text

    #«Начинки»
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click()
    error_element1 = driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[3]")
    assert "Начинки" in error_element1.text
    time.sleep(2)
    driver.quit()

main()