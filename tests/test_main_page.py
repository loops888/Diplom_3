import allure
import pytest

from pages.main_page import MainPage


class TestMainPage:


    @allure.title('Проверка клика на «Конструктор».')
    @allure.description(
        'Проверяем, что отобразилась форма конструктора после клика на «Конструктор».')
    def test_constructor_visibility(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_constructor_form()

    @allure.title('Проверка клика на «Лента заказов».')
    @allure.description(
        'Проверяем, что отобразилась форма ленты заказов после клика на «Лента заказов».')
    def test_orders_list_visibility(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_orders_list_form()

    @pytest.mark.parametrize(
        'ingredient, detail',
        [
            ('Флюоресцентная булка R2-D3', 'Флюоресцентная булка R2-D3'),
            ('Соус Spicy-X', 'Соус Spicy-X'),
            ('Мясо бессмертных моллюсков Protostomia', 'Мясо бессмертных моллюсков Protostomia')
        ]
    )
    @allure.title('Проверка клика на ингредиент.')
    @allure.description(
        'Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями.')
    def test_ingredients_details_visibility(self, driver, ingredient, detail):
        main_page = MainPage(driver)
        assert main_page.show_ingredients_details(ingredient, detail)

    @pytest.mark.parametrize(
        'ingredient, detail',
        [
            ('Флюоресцентная булка R2-D3', 'Флюоресцентная булка R2-D3'),
            ('Соус Spicy-X', 'Соус Spicy-X'),
            ('Мясо бессмертных моллюсков Protostomia', 'Мясо бессмертных моллюсков Protostomia')
        ]
    )
    @allure.title('Проверка клика по крестику в деталях ингредиента.')
    @allure.description(
        'Проверяем, что всплывающее окно закрывается кликом по крестику.')
    def test_close_ingredients_details_window(self, driver, ingredient, detail):
        main_page = MainPage(driver)
        assert main_page.close_ingredients_details(ingredient, detail)

    @pytest.mark.parametrize(
        'ingredient, count',
        [
            ('Флюоресцентная булка R2-D3', '2'),
            ('Соус Spicy-X', '1'),
            ('Мясо бессмертных моллюсков Protostomia', '1')
        ]
    )
    @allure.title('Проверка увеличения счетчика при добавлении ингредиента.')
    @allure.description(
        'Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается.')
    def test_add_ingredients_count_increase(self, driver, ingredient, count):
        main_page = MainPage(driver)
        assert main_page.count_ingredients(ingredient, count) == count

    @pytest.mark.parametrize(
        'ingredient',
        [
            ('Флюоресцентная булка R2-D3'),
            ('Соус Spicy-X'),
            ('Мясо бессмертных моллюсков Protostomia')
        ]
    )
    @allure.title('Проверка оформления заказа.')
    @allure.description(
        'Проверяем, что залогиненный пользователь может оформить заказ.')
    def test_authorized_user_confirm_order(self, login, ingredient):
        main_page = MainPage(login)
        assert main_page.confirm_order(ingredient) == 'Ваш заказ начали готовить'
