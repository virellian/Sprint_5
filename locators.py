from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт" (главная)
    login_button_main = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Кнопка "Войти в аккаунт" (точное совпадение)
    login_button_exact = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Поле Email
    email_input = (By.XPATH, "//input[@name='name']")

    # Поле Пароль
    password_input = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка "Войти"
    submit_button = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Кнопка "Оформить заказ"
    order_button = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')]")

    # Кнопка "Личный кабинет"
    cabinet_button = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]")

    # Кнопка "Выход" из аккаунта
    logout_button = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and normalize-space(text())='Выход']")

    # Ссылка "Зарегистрироваться"
    register_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and normalize-space(text())='Зарегистрироваться']")

    # Кнопка "Зарегистрироваться"
    register_button = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")

    # Сообщение об ошибке "Некорректный пароль"
    register_error = (By.XPATH, "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//*[normalize-space(text())='Некорректный пароль']")

    # Поле "Имя" при регистрации
    register_name_input = (By.XPATH, "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Имя']]//input")

    # Поле "Email" при регистрации
    register_email_input = (By.XPATH, "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Email']]//input")

    # Поле "Пароль" при регистрации
    register_password_input = (By.XPATH, "//fieldset[contains(@class, 'Auth_fieldset__1QzWN')]//div[label[normalize-space(text())='Пароль']]//input")

    # Ссылка "Восстановить пароль"
    restore_password_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and normalize-space(text())='Восстановить пароль']")

    # Ссылка "Войти" на форме восстановления пароля
    restore_login_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and normalize-space(text())='Войти']")

    # Любая ссылка с классом Auth_link__1fOlj
    auth_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")

    # Логотип (ссылка)
    logo_link = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']/a")

    # Ссылка на раздел "Конструктор"
    constructor_link = (By.XPATH, "//*[contains(@class, 'AppHeader_header__link__3D_hX') and contains(@class, 'AppHeader_header__link_active__1IkJo')]")

    # Вкладка "Соусы"
    sauce_tab = (By.XPATH, "//span[contains(text(), 'Соусы')]")

    # Вкладка "Булки"
    bread_tab = (By.XPATH, "//span[contains(text(), 'Булки')]")

    # Вкладка "Начинки"
    toppings_tab = (By.XPATH, "//span[contains(text(), 'Начинки')]")

    # Активная вкладка
    active_tab = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Активная вкладка "Соусы"
    active_tab_sauce = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Соусы')]")

    # Активная вкладка "Булки"
    active_tab_bread = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Булки')]")

    # Активная вкладка "Начинки"
    active_tab_toppings = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and contains(., 'Начинки')]")
