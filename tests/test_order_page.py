import allure

from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка отображения деталей заказа.')
    @allure.description(
        'Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями.')
    def test_order_details_visibility(self, driver):
        order_page = OrderPage(driver)
        assert order_page.show_order_details_form() == 'Cостав'

    @allure.title('Проверка отображения заказа пользователя в ленте заказов.')
    @allure.description(
        'Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    def test_show_user_order_from_orders_list(self, login):
        order_page = OrderPage(login)
        assert order_page.show_user_order()

    @allure.title('Проверка увеличения счётчика «Выполнено за всё время».')
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается.')
    def test_show_all_count_orders(self, login):
        order_page = OrderPage(login)
        all_time_count_before = order_page.show_all_time_done_orders_before_new()
        assert order_page.show_all_time_done_orders_after_new() > all_time_count_before

    @allure.title('Проверка увеличения счётчика «Выполнено за сегодня».')
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается.')
    def test_show_today_count_orders(self, login):
        order_page = OrderPage(login)
        today_count_before = order_page.show_today_done_orders_before_new()
        assert order_page.show_today_done_orders_after_new() > today_count_before

    @allure.title('Проверка нового заказа в разделе «В работе».')
    @allure.description(
        'Проверяем, что после оформления заказа его номер появляется в разделе «В работе».')
    def test_show_new_order_in_work(self, login):
        order_page = OrderPage(login)
        assert order_page.show_created_order_in_work()
