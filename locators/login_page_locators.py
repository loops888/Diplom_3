from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка "Войти" для авторизации.
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Поле для ввода Почты из окна регистрации.
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    # Поле для ввода Пароля из окна регистрации.
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
