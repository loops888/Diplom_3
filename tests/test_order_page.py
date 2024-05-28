import allure

from constants import Constants
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка отображения деталей заказа.')
    @allure.description(
        'Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями.')
    def test_order_details_visibility(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_orders_list()
        assert order_page.show_order_details_form() == 'Cостав'

    @allure.title('Проверка отображения заказа пользователя в ленте заказов.')
    @allure.description(
        'Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    def test_show_user_order_from_orders_list(self, login):
        main_page = MainPage(login)
        order_page = OrderPage(login)

        main_page.add_ingredients_to_burger(Constants.TEST_BURGER)
        main_page.confirm_order()
        order_number = f'{"#0" + order_page.get_number_of_created_order()}'
        main_page.go_to_orders_list()
        assert order_page.show_user_order(order_number)

    @allure.title('Проверка увеличения счётчика «Выполнено за всё время».')
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается.')
    def test_show_all_count_orders(self, login):
        main_page = MainPage(login)
        order_page = OrderPage(login)

        main_page.go_to_orders_list()
        all_time_count_before = order_page.show_all_time_done_orders()
        main_page.go_to_main_page()
        main_page.add_ingredients_to_burger(Constants.TEST_BURGER)
        main_page.confirm_order()
        order_page.get_number_of_created_order()
        main_page.go_to_orders_list()
        all_time_count_after = order_page.show_all_time_done_orders()
        assert all_time_count_after > all_time_count_before

    @allure.title('Проверка увеличения счётчика «Выполнено за сегодня».')
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается.')
    def test_show_today_count_orders(self, login):
        main_page = MainPage(login)
        order_page = OrderPage(login)

        main_page.go_to_orders_list()
        today_count_before = order_page.show_today_done_orders()
        main_page.go_to_main_page()
        main_page.add_ingredients_to_burger(Constants.TEST_BURGER)
        main_page.confirm_order()
        order_page.get_number_of_created_order()
        main_page.go_to_orders_list()
        today_count_after = order_page.show_today_done_orders()
        assert today_count_after > today_count_before

    @allure.title('Проверка нового заказа в разделе «В работе».')
    @allure.description(
        'Проверяем, что после оформления заказа его номер появляется в разделе «В работе».')
    def test_show_new_order_in_work(self, login):
        main_page = MainPage(login)
        order_page = OrderPage(login)

        main_page.add_ingredients_to_burger(Constants.TEST_BURGER)
        main_page.confirm_order()
        order_count = order_page.get_number_of_created_order()
        main_page.go_to_orders_list()
        assert order_page.show_created_order_in_work(order_count)
