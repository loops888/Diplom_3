import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Отображаем форму с деталями заказа.')
    def show_order_details_form(self):
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        self.click_on_element_action(OrderPageLocators.FIRST_ORDER_IN_LIST)
        return self.get_text_from_element(OrderPageLocators.ORDER_DETAILS)

    @allure.step('Создаем заказ и получаем его номер.')
    def create_order_and_get_number(self):
        self.drag_and_drop_element(OrderPageLocators.FIRST_INGREDIENT_IN_LIST,
                                   OrderPageLocators.INGREDIENTS_IN_BURGER_LIST)
        self.click_on_element_action(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.wait_for_element_to_change_text(OrderPageLocators.CREATED_ORDER_FORM, '9999')
        order_number = self.get_text_from_element(OrderPageLocators.CREATED_ORDER_FORM)
        self.click_on_element_action(OrderPageLocators.CREATED_ORDER_FORM_CLOSE)
        return order_number

    @allure.step('Находим заказ по номеру из раздела «История заказов».')
    def show_user_order(self):
        order_number = f'{"#0" + self.create_order_and_get_number()}'
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        order_in_list_formatted = self.format_locator(OrderPageLocators.CREATED_ORDER_IN_LIST, order_number)
        return self.get_text_from_element(order_in_list_formatted)

    @allure.step('Проверяем счётчик «Выполнено за всё время» до создания нового заказа.')
    def show_all_time_done_orders_before_new(self):
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        all_time_count_before = self.get_text_from_element(OrderPageLocators.ALL_TIME_COUNT)
        self.click_on_element_action(OrderPageLocators.LOGO_BUTTON)
        return all_time_count_before

    @allure.step('Проверяем счётчик «Выполнено за всё время» после создания нового заказа.')
    def show_all_time_done_orders_after_new(self):
        self.create_order_and_get_number()
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        return self.get_text_from_element(OrderPageLocators.ALL_TIME_COUNT)

    @allure.step('Проверяем счётчик «Выполнено за сегодня» до создания нового заказа.')
    def show_today_done_orders_before_new(self):
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        today_count_before = self.get_text_from_element(OrderPageLocators.TODAY_COUNT)
        self.click_on_element_action(OrderPageLocators.LOGO_BUTTON)
        return today_count_before

    @allure.step('Проверяем счётчик «Выполнено за сегодня» после создания нового заказа.')
    def show_today_done_orders_after_new(self):
        self.create_order_and_get_number()
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        return self.get_text_from_element(OrderPageLocators.TODAY_COUNT)

    @allure.step('Проверяем заказ в разделе «В работе».')
    def show_created_order_in_work(self):
        order_count = self.create_order_and_get_number()
        self.click_on_element(OrderPageLocators.ORDERS_LIST_BUTTON)
        order_number_in_work_formatted = self.format_locator(OrderPageLocators.ORDER_NUMBER_IN_WORK, order_count)
        return self.get_text_from_element(order_number_in_work_formatted)
