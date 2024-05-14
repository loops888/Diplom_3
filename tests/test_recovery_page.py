import allure
from pages.recovery_page import RecoveryPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль».')
    @allure.description(
        'Проверяем, что перешли в соответствующее окно с кнопкой восстановления пароля.')
    def test_recovery_page_transition(self, driver):
        recovery_page = RecoveryPage(driver)
        assert recovery_page.go_to_recovery_window() == 'Восстановить'

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить».')
    @allure.description(
        'Проверяем, что после ввода почты и клика по кнопке «Восстановить» нам предлагают ввести код из письма.')
    def test_put_email_for_recovery(self, driver):
        recovery_page = RecoveryPage(driver)
        assert recovery_page.go_to_recovery_confirm_window() == 'Введите код из письма'

    @allure.title("Проверка видимости пароля.")
    @allure.description(
        'Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_recovery_form_field_password_active(self, driver):
        recovery_page = RecoveryPage(driver)
        assert recovery_page.change_password_visibility() == 'text'
