from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопка "Лента заказов".
    ORDERS_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # Окно деталей по заказу.
    ORDER_DETAILS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    # Добавленные в бургер ингредиенты.
    INGREDIENTS_IN_BURGER_LIST = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    # Первый заказ в списке.
    FIRST_ORDER_IN_LIST = (By.XPATH, "/descendant::div[@class='OrderHistory_textBox__3lgbs mb-6'][position() = (1)]")
    # Первый ингредиент в списке.
    FIRST_INGREDIENT_IN_LIST = (By.XPATH, "/descendant::a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][position() = (1)]")
    # Кнопка "Оформить заказ".
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # Окно созданного заказа.
    CREATED_ORDER_FORM = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # Кнопка закрытия окна созданного заказа.
    CREATED_ORDER_FORM_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # Созданный заказ в списке заказов.
    CREATED_ORDER_IN_LIST = (By.XPATH, ".//p[@class = 'text text_type_digits-default' and text()='{}']")
    # Счетчик созданных заказов за все время.
    ALL_TIME_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (1)]")
    # Счетчик созданных заказов за все сегодня.
    TODAY_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (2)]")
    # Поле отображения заказов в работе.
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2' and text()='{}']")
    # Кнопка с логотипом для выхода на главную страницу.
    LOGO_BUTTON = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
