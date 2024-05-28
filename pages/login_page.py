import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Вводим емейл пользователя.')
    def print_user_email(self, email):
        self.insert_text_in_field(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Вводим пароль пользователя.')
    def print_user_password(self, password):
        self.insert_text_in_field(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Авторизируем пользователя.')
    def confirm_user_authorization(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Проверяем отображение окна авторизации.')
    def show_authorization_form(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_BUTTON)
