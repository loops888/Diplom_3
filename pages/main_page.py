import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем личный кабинет.')
    def go_to_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Открываем ленту заказов.')
    def go_to_orders_list(self):
        self.click_on_element(MainPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('Ждем прогрузки главной страницы.')
    def wait_for_main_page(self):
        self.find_element_with_waiting(MainPageLocators.MAIN_PAGE)

    @allure.step('Возвращаемся на главную страницу через кнопку с логотипом.')
    def go_to_main_page(self):
        self.click_on_element_action(MainPageLocators.LOGO_BUTTON)

    @allure.step('Отображаем форму с конструктором.')
    def show_constructor_form(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element_with_waiting(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Отображаем детали по ингредиентам.')
    def show_ingredients_details(self, ingredient, detail):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        ingredient_formatted = self.format_locator(MainPageLocators.INGREDIENT_BUTTON, ingredient)
        detail_formatted = self.format_locator(MainPageLocators.INGREDIENT_DETAILS_FORM, detail)
        self.scroll_to_element(ingredient_formatted)
        self.click_on_element(ingredient_formatted)
        return self.find_element_with_waiting(detail_formatted)

    @allure.step('Закрываем детали по ингредиентам.')
    def close_ingredients_details(self, ingredient, detail):
        self.show_ingredients_details(ingredient, detail)
        self.click_on_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE)
        return self.find_element_with_waiting(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Перетаскиваем ингредиенты в бургер.')
    def add_ingredients_to_burger(self, ingredient):
        ingredient_formatted = self.format_locator(MainPageLocators.INGREDIENT_BUTTON, ingredient)
        self.scroll_to_element(ingredient_formatted)
        self.drag_and_drop_element(ingredient_formatted, MainPageLocators.INGREDIENTS_IN_BURGER_LIST)

    @allure.step('Смотрим счетчик ингредиентов.')
    def count_ingredients(self, ingredient, count):
        self.add_ingredients_to_burger(ingredient)
        count_formatted = self.format_locator(MainPageLocators.INGREDIENT_COUNT, count)
        return self.get_text_from_element(count_formatted)

    @allure.step('Создаем заказ.')
    def confirm_order(self):
        self.click_on_element(MainPageLocators.CONFIRM_ORDER_BUTTON)
        return self.get_text_from_element(MainPageLocators.CONFIRM_ORDER_FORM)
