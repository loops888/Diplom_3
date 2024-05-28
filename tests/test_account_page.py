import allure
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountPage:

    @allure.title('Проверка клика на «Личный кабинет».')
    @allure.description(
        'Проверяем, что перешли по клику на «Личный кабинет» в профиль пользователя.')
    def test_account_page_transition(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)

        main_page.go_to_personal_account()
        assert account_page.show_personal_account_window() == 'Профиль'

    @allure.title('Проверка клика на меню «История» из личного кабинета.')
    @allure.description(
        'Проверяем, что по клику на «История» перешли в историю заказов пользователя.')
    def test_account_history_visibility(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)

        main_page.go_to_personal_account()
        assert account_page.show_personal_orders_history() == 'page'

    @allure.title('Проверка клика на «Выход» из личного кабинета.')
    @allure.description(
        'Проверяем, что по клику на «Выход» вышли из профиля и перешли в форму авторизации.')
    def test_log_out_from_account(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)
        login_page = LoginPage(login)

        main_page.go_to_personal_account()
        account_page.log_out_from_personal_account()
        assert login_page.show_authorization_form() == 'Войти'
