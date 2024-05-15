from selenium.webdriver.common.by import By


class MainPageLocators:
    # Ссылка на вход в "Личный Кабинет".
    PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")
    # Кнопка "Конструктор".
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    # Форма конструктора.
    CONSTRUCTOR_FORM = (By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")
    # Кнопка "Лента заказов".
    ORDERS_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # Форма ленты заказов.
    ORDERS_LIST_FORM = (By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']")
    # Кнопка ингредиента из конструктора.
    INGREDIENT_BUTTON = (By.XPATH, ".//p[@class = 'BurgerIngredient_ingredient__text__yp3dH' and text()='{}']")
    # Кнопка ингредиента из конструктора.
    INGREDIENT_DETAILS_FORM = (By.XPATH, ".//p[@class = 'text text_type_main-medium mb-8' and text()='{}']")
    # Кнопка закрытия деталей ингредиента.
    INGREDIENT_DETAILS_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # Счетчик количества ингредиентов на добавление в бургер.
    INGREDIENT_COUNT = (By.XPATH, ".//p[@class = 'counter_counter__num__3nue1' and text()='{}']")
    # Добавленные в бургер ингредиенты.
    INGREDIENTS_IN_BURGER_LIST = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    # Кнопка "Оформить заказ".
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # Форма подтверждения оформления заказа.
    CONFIRM_ORDER_FORM = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")
