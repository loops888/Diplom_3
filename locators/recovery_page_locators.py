from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    # Ссылка на переход в окно "Восстановление пароля".
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    # Кнопка "Восстановить" в окне "Восстановление пароля".
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    # Поле "Введите код из письма" в окне "Восстановление пароля".
    RECOVERY_CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    # Поле "Введите новый пароль" в окне "Восстановление пароля".
    RECOVERY_PASSWORD_FIELD = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = 'Введите новый пароль']")
    # Кнопка показать/скрыть пароль.
    PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']")
