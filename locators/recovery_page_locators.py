from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    # Кнопка "Войти в аккаунт".
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Ссылка на переход в окно "Восстановление пароля".
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    # Кнопка "Восстановить" в окне "Восстановление пароля".
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    # Поле для ввода Почты из окна регистрации.
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    # Поле для ввода Пароля из окна регистрации.
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    # Поле "Введите код из письма" в окне "Восстановление пароля".
    RECOVERY_CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    # Поле "Введите новый пароль" в окне "Восстановление пароля".
    RECOVERY_PASSWORD_FIELD = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = 'Введите новый пароль']")
    # Кнопка показать/скрыть пароль.
    PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']")
