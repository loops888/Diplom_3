import allure

from constants import Constants
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль».')
    @allure.description(
        'Проверяем, что перешли в соответствующее окно с кнопкой восстановления пароля.')
    def test_recovery_page_transition(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)

        main_page.go_to_personal_account()
        assert recovery_page.go_to_recovery_window() == 'Восстановить'

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить».')
    @allure.description(
        'Проверяем, что после ввода почты и клика по кнопке «Восстановить» нам предлагают ввести код из письма.')
    def test_put_email_for_recovery(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.print_user_email(Constants.TEST_EMAIL)
        assert recovery_page.go_to_recovery_confirm_window() == 'Введите код из письма'

    @allure.title("Проверка видимости пароля.")
    @allure.description(
        'Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_recovery_form_field_password_active(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.print_user_email(Constants.TEST_EMAIL)
        recovery_page.go_to_recovery_confirm_window()
        login_page.print_user_password(Constants.TEST_PASSWORD)
        assert recovery_page.change_password_visibility() == 'text'
