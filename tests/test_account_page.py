import allure
from pages.account_page import AccountPage


class TestAccountPage:

    @allure.title('Проверка клика на «Личный кабинет».')
    @allure.description(
        'Проверяем, что перешли по клику на «Личный кабинет» в профиль пользователя.')
    def test_account_page_transition(self, login):
        account_page = AccountPage(login)
        assert account_page.go_to_personal_account_window() == 'Профиль'

    @allure.title('Проверка клика на меню «История» из личного кабинета.')
    @allure.description(
        'Проверяем, что по клику на «История» перешли в историю заказов пользователя.')
    def test_account_history_visibility(self, login):
        account_page = AccountPage(login)
        assert account_page.go_to_personal_orders_history() == 'page'

    @allure.title('Проверка клика на «Выход» из личного кабинета.')
    @allure.description(
        'Проверяем, что по клику на «Выход» вышли из профиля и перешли в форму авторизации.')
    def test_log_out_from_account(self, login):
        account_page = AccountPage(login)
        assert account_page.log_out_from_personal_account() == 'Войти'
