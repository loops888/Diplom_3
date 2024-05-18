from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма ленты заказов.
    ORDERS_LIST_FORM = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    # Окно деталей по заказу.
    ORDER_DETAILS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    # Первый заказ в списке.
    FIRST_ORDER_IN_LIST = (By.XPATH, "/descendant::div[@class='OrderHistory_textBox__3lgbs mb-6'][position() = (1)]")
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
