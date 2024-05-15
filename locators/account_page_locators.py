from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Ссылка на вход в "Личный Кабинет".
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    # Ссылка на отображение личного профиля пользователя.
    ACCOUNT_PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")
    # Ссылка на отображение личной истории заказов.
    ACCOUNT_HISTORY_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")
    # Активная история заказов.
    ACCOUNT_HISTORY_ACTIVE = (By.XPATH, ".//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and contains(text(),'История заказов')]")
    # Ссылка на выход из профиля пользователя.
    ACCOUNT_EXIT_LINK = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Форма для авторизации пользователя.
    LOGIN_WINDOW = (By.XPATH, "//button[contains(text(),'Войти')]")
